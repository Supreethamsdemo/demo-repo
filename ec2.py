import boto3
regions="us-east-1"
for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']}])
    cw = boto3.client('cloudwatch', region_name=region)
    for instance in running_instances:
        instance_profile = 'N/A';
        if instance.iam_instance_profile:
            instance_profile = instance.iam_instance_profile['Arn']
            print(region,
                instance.id,
                instance.instance_type,
                instance_profile)
