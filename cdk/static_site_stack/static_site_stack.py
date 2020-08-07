from aws_cdk import (
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_cloudfront as cf,
    aws_s3 as s3,
    core
)

certificate_arn = "arn:aws:acm:us-east-1:667206377715:certificate/62206b2f-d963-4ce2-841a-37a6d8705ab4"
hosted_zone_id = "Z05672093954N8JIZRDO5"


class StaticSiteStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, env: str, domain: str, **kwargs) -> None:
        self.env = env
        self.domain = domain
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, 
            f"{env}bucket", 
            bucket_name=f"{env}.{domain}", 
            website_index_document="index.html", 
            removal_policy=core.RemovalPolicy.DESTROY, 
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

        core.CfnOutput(self, f"{env}bucketname", value=bucket.bucket_name)
        core.CfnOutput(self, f"{env}bucketsite",
                       value=bucket.bucket_website_url)


        oai = cf.OriginAccessIdentity(
            self,
            f"OriginIdentity-{env}-{domain}",
        )

        alias_configuration = cf.AliasConfiguration(
            acm_cert_ref=certificate_arn,
            names=[f"{env}.{domain}"],
            ssl_method=cf.SSLMethod.SNI,
            security_policy=cf.SecurityPolicyProtocol.TLS_V1_1_2016
        )

        cf_behavior_dict = {
            "dev": cf.Behavior(is_default_behavior=True, min_ttl=core.Duration.seconds(0), max_ttl=core.Duration.seconds(3600), default_ttl=core.Duration.seconds(3600)),
            "stg": cf.Behavior(is_default_behavior=True),
            "prod": cf.Behavior(is_default_behavior=True)
        }

        source_config = cf.SourceConfiguration(
            s3_origin_source=cf.S3OriginConfig(
                s3_bucket_source=bucket,
                origin_access_identity=oai
            ),
            behaviors=[cf_behavior_dict[env]]
        )

        cf_dist = cf.CloudFrontWebDistribution(
            self,
            f"{env}-static-site-distribution",
            alias_configuration=alias_configuration,
            origin_configs=[source_config],
            viewer_protocol_policy=cf.ViewerProtocolPolicy.REDIRECT_TO_HTTPS
        )

        core.CfnOutput(self, "dist_id", value=cf_dist.distribution_id)
        core.CfnOutput(self, "dist_domain_name", value=cf_dist.domain_name)

        # Route53 alias record for the CloudFront Distribution
        hosted_zone = route53.HostedZone.from_hosted_zone_attributes(
            self,
            id="static-site-hosted-zone-id",
            hosted_zone_id=hosted_zone_id,
            zone_name=domain
        )

        route53.ARecord(
            self,
            'static-site-alias-record',
            record_name=f"{env}.{domain}",
            target=route53.AddressRecordTarget.from_alias(targets.CloudFrontTarget(cf_dist)),
            zone=hosted_zone
        )
