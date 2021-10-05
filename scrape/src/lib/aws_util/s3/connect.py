import boto3
from boto3.resources import factory



def connect_to_bucket(
  bucket_name: str,
) -> factory.ResourceFactory:
  s3 = boto3.resource('s3')
  return s3.Bucket(bucket_name)
