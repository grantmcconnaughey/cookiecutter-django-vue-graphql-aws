from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_s3_deployment as s3deploy,
)


class FrontendStack(core.Stack):

    CERTIFICATE_ARN = (
        'arn:aws:acm:us-east-1:634337638384:certificate/1c0b3eba-38cf-446a-88f0-24073910768f'
    )
    DOMAIN_NAME = 'www.{{cookiecutter.domain_name}}'
    ROOT_DOMAIN_NAME = '{{cookiecutter.domain_name}}'

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        website_bucket = s3.Bucket(
            self,
            'FrontendBucket',
            versioned=True,
            website_index_document='index.html',
            website_error_document='index.html',
            public_read_access=True,
        )

        distribution = cloudfront.CloudFrontWebDistribution(
            self,
            'Distribution',
            alias_configuration=cloudfront.AliasConfiguration(
                acm_cert_ref=self.CERTIFICATE_ARN, names=[self.DOMAIN_NAME],
            ),
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(s3_bucket_source=website_bucket),
                    behaviors=[cloudfront.Behavior(is_default_behavior=True, compress=True)],
                )
            ],
            error_configurations=[
                cloudfront.CfnDistribution.CustomErrorResponseProperty(
                    error_code=403,
                    error_caching_min_ttl=300,
                    response_code=200,
                    response_page_path='/index.html',
                ),
                cloudfront.CfnDistribution.CustomErrorResponseProperty(
                    error_code=404,
                    error_caching_min_ttl=300,
                    response_code=200,
                    response_page_path='/index.html',
                ),
            ],
        )

        s3deploy.BucketDeployment(
            self,
            'DeployWithInvalidation',
            sources=[s3deploy.Source.asset('../frontend/dist/')],
            destination_bucket=website_bucket,
            distribution=distribution,
            distribution_paths=['/*'],
        )

        # Django staticfiles
        s3.Bucket(
            self, 'StaticAssetsBucket', public_read_access=True,
        )

        # non-www to www redirection
        redirect_bucket = s3.Bucket(
            self,
            'RedirectedBucket',
            bucket_name=self.ROOT_DOMAIN_NAME,
            website_redirect={'host_name': 'https://www.{{cookiecutter.domain_name}}'},
            public_read_access=True,
        )
        cloudfront.CloudFrontWebDistribution(
            self,
            'RedirectDistribution',
            alias_configuration=cloudfront.AliasConfiguration(
                acm_cert_ref=self.CERTIFICATE_ARN, names=[self.ROOT_DOMAIN_NAME],
            ),
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(s3_bucket_source=redirect_bucket),
                    behaviors=[cloudfront.Behavior(is_default_behavior=True)],
                )
            ],
        )
