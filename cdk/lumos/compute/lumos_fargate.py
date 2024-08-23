from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_s3 as s3,
    aws_elasticloadbalancingv2 as elbv2,
    Stack,
    CfnOutput
)

from constructs import Construct

class FargateStack(Stack):
    def __init__(
            self,
            scope: Construct,
            id: str,
            ecr_repository: ecr.IRepository,
            vpc: ec2.IVpc,
            load_balancer,
            s3_bucket: s3.IBucket, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cluster = ecs.Cluster(
            self,
            "LumosCluster",
            vpc=vpc
        )

        task_definition = ecs.FargateTaskDefinition(
            self,
            "LumosTaskDefinition",
            cpu=256,
            memory_limit_mib=512
        )

        lumos_docker_image = ecs.ContainerImage.from_ecr_repository(
            repository=ecr_repository,
            tag="latest"
        )

        container = task_definition.add_container(
            "LumosContainer",
            image=lumos_docker_image,
            memory_reservation_mib=512
        )

        container.add_port_mappings(
            ecs.PortMapping(
                container_port=8000
            )
        )

        fargate_service = ecs.FargateService(
            self,
            "LumosFargateService",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=2
        )

        s3_bucket.grant_read(task_definition.task_role)

        load_balancer._listener.add_targets(
            'LumosTargetGroup',
            port=80,
            targets=[fargate_service]
        )
