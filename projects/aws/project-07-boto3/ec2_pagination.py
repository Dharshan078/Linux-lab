import boto3

ec2 = boto3.client("ec2")

paginator = ec2.get_paginator("describe_instances")

for page in paginator.paginate():
    print(page)