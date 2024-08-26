from aws_cdk import (
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_elasticloadbalancingv2 as elbv2,
    Stack,
    Fn
)

from constructs import Construct


class DNSStack(Stack):
    def __init__(
            self,
            scope: Construct,
            id: str,
            load_balancer,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        hosted_zone_id = 'Z00528603RL8W30CQULIV'

        hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
            self,
            "LumosHostedZone",
            hosted_zone_id=hosted_zone_id,
            zone_name='illuminatewithlumos.com'
        )

        route53.ARecord(
            self,
            'LumosAliasRecord',
            record_name='www',
            target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(load_balancer.load_balancer)),
            zone=hosted_zone,
        )
