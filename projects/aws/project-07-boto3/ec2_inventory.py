#########################################################
# AWS EC2 Inventory
# Author: Sivadharshan
# Version: 1.3
# 1.0: Raw code just to print the instance information
# 1.1: Added functions, Clean code
# 1.2: Added try and exceptions [Clinet and BotoCore Error]
# 1.3: Using filter to filter out only running EC2 instances
# 1.4: Pagination started
#########################################################


import boto3
from botocore.exceptions import ClientError, BotoCoreError

def main():
    print("="*40)
    print("RUNNING EC2 INSTANCE INVENTORY")
    print("="*40)
    get_instance = get_instances()
    if not get_instance:
        print("No running EC2 instances found")
        return
    else:
         for instance in get_instance:
            print("Reservation ID   :",instance["ReservationId"])
            for instances in instance["Instances"]:
                print("Instance ID      :",instances["InstanceId"])
                print("Instance Type    :",instances["InstanceType"])
                print("Instance State   :",instances["State"]["Name"])
                print("Private IP       :",instances.get("PrivateIpAddress","N/A"))
                print("Availability Zone:",instances["Placement"]["AvailabilityZone"])
          
def get_instances():
    try:
        ec2 = boto3.client("ec2")
        instance_filter = [
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            },
        ]
        response = ec2.describe_instances(Filters=instance_filter)
        return response["Reservations"]
    except ClientError as error:
        print(f"AWS API error: {error}")
        return []
    except BotoCoreError as error:
        print(f"Boto3 error: {error}")

if __name__ == "__main__":
     main()