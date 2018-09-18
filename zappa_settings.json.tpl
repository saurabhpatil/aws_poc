{
    "dev": {
        "aws_region": "us-east-1",
        "django_settings": "aws_poc.settings",
        "profile_name": "default",
        "project_name": "atlas-webapp",
        "runtime": "python3.6",
        "s3_bucket": "ct-atlas-zappa-bucket",
        "environment_variables": {"RDS_DB_NAME": $RDS_DB_NAME,
                                  "RDS_USERNAME": $RDS_USERNAME,
                                  "RDS_PASSWORD": $RDS_PASSWORD,
                                  "RDS_HOSTNAME": $RDS_HOSTNAME,
                                  "RDS_PORT": $RDS_PORT},
        "vpc_config": {
            "SubnetIds": [ "subnet-94ead9e2" ],
            "SecurityGroupIds": [ "sg-b97c3df2" ]
        },
        "manage_roles": false,
        "role_name": "ct-atlas-zappa-role",
        "role_arn": "arn:aws:iam::585807852923:role/ct-atlas-zappa-role",
        "keep_warm": false,
        "timeout_seconds": 60
    }
}