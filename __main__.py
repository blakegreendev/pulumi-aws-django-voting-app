"""An AWS Python Pulumi program"""
import json
import base64
import pulumi
import pulumi_aws as aws
import pulumi_docker as docker
import pulumi_mysql as mysql

config = pulumi.Config()
sql_admin_name = config.require("sql-admin-name")
sql_admin_password = config.require_secret("sql-admin-password")
sql_user_name = config.require("sql-user-name")
sql_user_password = config.require_secret("sql-user-password")
availability_zone = pulumi.Config("aws").get("region")

django_admin_name = config.require("django-admin-name")
django_admin_password = config.require_secret("django-admin-password")

django_secret_key = config.require_secret("django-secret-key")

app_cluster = aws.ecs.Cluster("app-cluster")