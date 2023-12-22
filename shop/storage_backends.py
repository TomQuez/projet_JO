from storages.backends.s3boto3 import S3Boto3Storage

from decouple import config
AWS_STORAGE_BUCKET_NAME=config('AWS_STORAGE_BUCKET_NAME')
class MediaStorage(S3Boto3Storage):
    location='media'
    file_overwrite=False
    custom_domain='.s3.eu-north-1.amazonaws.com'
    