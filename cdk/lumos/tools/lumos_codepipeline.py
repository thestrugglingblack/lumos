from aws_cdk import (
    aws_codebuild as codebuild,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_ecr as ecr,
    Stack,
    aws_secretsmanager as sm,
    aws_iam as iam

)

from constructs import Construct

class CICDStack(Stack):
    def __init__(
            self,
            scope: Construct,
            id: str,
            ecr_repository: ecr.IRepository,
            secrets,
            **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        role = iam.Role(
            self,
            'LumosCodeBuildRole',
            assumed_by=iam.ServicePrincipal("codebuild.amazonaws.com")
        )

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ContainerRegistryPowerUser"))


        # Define the CodeBuild project
        codebuild_project = codebuild.PipelineProject(
            self,
            "LumosBuild",
            role= role,
            build_spec=codebuild.BuildSpec.from_object({
                "version": "0.2",
                "phases": {
                    "install": {
                        "commands": [

                            'curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -',
                            'apt-get update'
                        ],
                    },
                    "build": {
                        "commands": [
                            f"docker build -t {ecr_repository.repository.repository_uri}:latest .",
                        ],
                    },
                    "post_build": {
                        "commands": [
                            f"$(aws ecr get-login --no-include-email --region {self.region})",
                            f"docker push {ecr_repository.repository.repository_uri}:latest",
                        ],
                    },
                },
            }),
            environment=codebuild.BuildEnvironment(
                privileged=True,
            ),
        )

        source_artifact = codepipeline.Artifact()

        # Define the CodePipeline
        codepipeline.Pipeline(
            self,
            "LumosPipeline",
            stages=[
                codepipeline.StageProps(
                    stage_name="Retrieve_Source",
                    actions=[
                        codepipeline_actions.GitHubSourceAction(
                            action_name="GitHub",
                            output=source_artifact,
                            oauth_token=secrets,
                            owner="thestrugglingblack",
                            repo="lumos",
                            branch="main",
                        ),
                    ],
                ),
                codepipeline.StageProps(
                    stage_name="Build_Push_Docker_Image",
                    actions=[
                        codepipeline_actions.CodeBuildAction(
                            action_name="CodeBuild",
                            project=codebuild_project,
                            input=source_artifact,
                            outputs=[codepipeline.Artifact()],
                        ),
                    ],
                ),
            ],
        )