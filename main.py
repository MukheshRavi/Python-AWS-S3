import boto3 as b
import os
print(os.getenv('Access Key'))
try:
    s3=b.client('s3',aws_access_key_id=os.getenv('Access Key')
    ,aws_secret_access_key=os.getenv('Secret Key'))

    s3.download_file('test-aws-python','industry.csv','industry.csv')

except:
    print('Error occured')

