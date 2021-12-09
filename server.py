from config import *
import boto3

def startEC2():
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.start_instances(InstanceIds=INSTANCE_IDS)

def stopEC2():
    ec2 = boto3.client('ec2', region_name=REGION)
    ec2.stop_instances(InstanceIds=INSTANCE_IDS)
