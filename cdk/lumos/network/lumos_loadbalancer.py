from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elbv2,
    Stack,
    CfnOutput
)

from constructs import Construct

class LoadBalancerStack(Stack):

    @property
    def load_balancer(self):
        return self._load_balancer

    def __init__(
            self,
            scope: Construct,
            id: str,
            vpc: ec2.IVpc,
            security_group: ec2.ISecurityGroup,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self._load_balancer = elbv2.ApplicationLoadBalancer(
            self,
            'LumosLoadBalancer',
            vpc=vpc,
            internet_facing=True
        )

        self._listener = self.load_balancer.add_listener(
            "LumosListener",
            port=80,
            open=True
        )
