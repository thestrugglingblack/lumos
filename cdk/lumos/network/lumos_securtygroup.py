from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class SecurityGroupStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # # # Create WISD24 Lumos VPC
        self.vpc = ec2.Vpc(
            self,
            'LumosVPC',
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name='Private',
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    cidr_mask=24
                )
            ],
            nat_gateways=1
        )

        # # # Create WISD24 Lumos Security Group
        self.security_group = ec2.SecurityGroup(
            self, "LumosSecurityGroup",
            vpc=self.vpc,
            description="Allow inbound traffic on port 80",
            allow_all_outbound=True
        )

    # # # Add Ingress Rules for traffic to come in through port 80 and port 8000, respectively
        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow inbound traffic on port 80"
        )

        self.security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(8000),
            description="Allow inbound traffic on port 80"
        )
