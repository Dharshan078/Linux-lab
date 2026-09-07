#########################################################
# AWS EC2 Inventory
# Author: Sivadharshan
# Version: 1.3
# 1.0: Raw code just to print the instance information
# 1.1: Added functions, Clean code
# 1.2: Added try and exceptions [Clinet and BotoCore Error]
# 1.3: Using filter to filter out only running EC2 instances
# 1.4: Pagination completed to handle more than 1000s of instances
#########################################################


import boto3
from botocore.exceptions import ClientError, BotoCoreError

def main():
    print("="*40)
    print("RUNNING EC2 INSTANCE INVENTORY")
    print("="*40)
    all_reservations, total_pages = get_instances()
    if not all_reservations:
        print("No running EC2 instances found")
        print("Total Pages = ", total_pages)
        return

    total_running_instances = 0
    for instance in all_reservations:
        print("Reservation ID   :",instance["ReservationId"])
        for instances in instance["Instances"]:
            print("Instance ID      :",instances["InstanceId"])
            print("Instance Type    :",instances["InstanceType"])
            print("Instance State   :",instances["State"]["Name"])
            print("Private IP       :",instances.get("PrivateIpAddress","N/A"))
            print("Availability Zone:",instances["Placement"]["AvailabilityZone"])
            print("="*40)
            total_running_instances += 1
    print("Total Running Instances = ", total_running_instances)
    print("Total Pages = ", total_pages)
          
def get_instances():
    try:
        ec2 = boto3.client("ec2")
        instance_filter = [
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }, 
        ]
        paginator = ec2.get_paginator("describe_instances")
        total_pages = 0
        all_reservations = []
        for page in paginator.paginate(Filters=instance_filter):
            reservations = page["Reservations"]
            all_reservations.extend(reservations)
            total_pages += 1

        return all_reservations, total_pages
    except ClientError as error:
        print(f"AWS API error: {error}")
        return [], None
    except BotoCoreError as error:
        print(f"Boto3 error: {error}")
        return [], None

if __name__ == "__main__":
     main()