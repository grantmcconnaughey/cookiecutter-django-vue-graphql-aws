from aws_cdk import (
    core,
    aws_rds as rds,
    aws_ec2 as ec2,
)


class NetworkingAndDBStack(core.Stack):

    DB_PORT = 5432
    DB_PASSWORD_PARAM_NAME = '/{{cookiecutter.project_slug}}/db-password'

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, 'VPC', nat_gateways=1)

        db_security_group = ec2.SecurityGroup(
            self, 'SecurityGroup', vpc=vpc, allow_all_outbound=False
        )
        db_security_group.add_ingress_rule(
            ec2.Peer.ipv4(vpc.vpc_cidr_block),
            ec2.Port.tcp(self.DB_PORT),
            description='Allow inbound traffic from within VPC',
        )

        rds.DatabaseInstance(
            self,
            'RDS',
            database_name='{{cookiecutter.project_slug}}',
            master_username='master',
            master_user_password=core.SecretValue.ssm_secure(self.DB_PASSWORD_PARAM_NAME, '1'),
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            engine_version='11.6',
            vpc=vpc,
            port=self.DB_PORT,
            instance_class=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO,
            ),
            allocated_storage=20,
            removal_policy=core.RemovalPolicy.DESTROY,
            deletion_protection=False,
            security_groups=[db_security_group],
        )
