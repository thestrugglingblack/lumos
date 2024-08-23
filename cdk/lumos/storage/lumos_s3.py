import os
from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    RemovalPolicy
)
from constructs import Construct

from ..utils.util import zip_dir

class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # # Create WISD24 Lumos Data S3 Bucket
        self.bucket = s3.Bucket(
            self, "LumosDataBucket",
            bucket_name="wisd24-lumos-data-bucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # # # Zip the data directory for upload to S3
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, '../data/')

        zip_dir('/Users/zuri/Documents/Explore/lumos/data', 'data.zip')

        s3deploy.BucketDeployment(
                self, "LumosDeployData",
                sources=[s3deploy.Source.asset(data_dir + "../../data/data.zip")],
                destination_bucket=self.bucket,
                retain_on_delete=False
        )

