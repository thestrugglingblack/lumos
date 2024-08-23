from aws_cdk import (
    Stack,
    aws_ecr as ecr,
    RemovalPolicy
)
from constructs import Construct

class EcrStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # # Create WISD24 Lumos ECR Repository
        self.repository = ecr.Repository(
            self, "LumosRepository",
            repository_name="wisd24/lumos-shiny-application",
            removal_policy=RemovalPolicy.DESTROY
        )
