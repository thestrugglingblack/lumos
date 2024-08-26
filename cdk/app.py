#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dotenv import load_dotenv

from lumos.storage.lumos_ecr import EcrStack
from lumos.storage.lumos_s3 import S3Stack
from lumos.network.lumos_securtygroup import SecurityGroupStack
from lumos.compute.lumos_fargate import FargateStack
from lumos.network.lumos_loadbalancer import LoadBalancerStack
from lumos.network.lumos_dns import DNSStack

load_dotenv('../.env')

account_id = os.getenv('AWS_ID')

app = cdk.App()

ecr_stack = EcrStack(
    app,
    "EcrStack",
    env=cdk.Environment(account=account_id, region='us-east-1')
)

s3_stack = S3Stack(
    app,
    "S3Stack",
    env=cdk.Environment(account=account_id, region='us-east-1')
)

securitygroup_stack = SecurityGroupStack(
    app,
    "SecurityGroupStack",
    env=cdk.Environment(account=account_id, region='us-east-1')
)

loadbalancer_stack = LoadBalancerStack(
    app,
    "LoadBalancerStack",
    security_group=securitygroup_stack.security_group,
    vpc=securitygroup_stack.vpc,
    env=cdk.Environment(account=account_id, region='us-east-1')
)

dns_stack = DNSStack(
    app,
    'DNSStack',
    load_balancer=loadbalancer_stack,
    env=cdk.Environment(account=account_id, region='us-east-1')
)

fargatestack = FargateStack(
    app, "FargateStack",
    ecr_repository=ecr_stack.repository,
    s3_bucket=s3_stack.bucket,
    vpc=securitygroup_stack.vpc,
    load_balancer=loadbalancer_stack,
    env=cdk.Environment(account=account_id, region='us-east-1')
)



app.synth()
