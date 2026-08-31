import boto3

def main():
    identity = get_identity()
    print("User ID  :",identity["UserId"])
    print("Account  :",identity["Account"])
    print("ARN      :",identity["Arn"])
    return identity

def get_identity():
    sts = boto3.client("sts")
    response = sts.get_caller_identity()
    return response

if __name__ == "__main__":
    main()
