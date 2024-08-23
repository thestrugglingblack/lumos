import os
from aws_cdk import (
    aws_secretsmanager as sm,
    aws_ecs as ecs,
    Stack
)

from constructs import Construct
from dotenv import load_dotenv

load_dotenv('../.env')

account_id = os.getenv('AWS_ID')
class SecretsStack(Stack):
    def __init__(
            self,
            scope: Construct,
            id: str,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        gh_secret_name = 'dev/lumos/github_access_token'

        gh_secret_arn = f'arn:aws:secretsmanager:us-east-1:{account_id}:secret:dev/lumos/github_access_token-SWr0AH'
        gh_secrets = sm.Secret.from_secret_name_v2(
            self,
            'LumosGHToken',
            gh_secret_name
        )



        self.gh_token = gh_secrets.secret_value_from_json('GITHUB_ACCESS_TOKEN')