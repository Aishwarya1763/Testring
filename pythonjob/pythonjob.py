import sys
import json
import snowflake.connector
from awsglue.utils import getResolvedOptions
import boto3 as boto3
import requests





conn = snowflake.connector.connect(
user="aishwarya",
password="Aishu@1763",
account="exb42038.us-east-1",
warehouse="COMPUTE_VM",
database="OUR_FIRST_DB",
schema="PUBLIC",
role="ACCOUNTADMIN"
)

cursor = conn.cursor()

def process():
    URL = "https://api.prod.synop.ai/api/assets"
    headers = {
        'Content-type': 'application/json',
        'x-api-key': 'ThWeX2th8Z2eTV3dBvKzw6bMidbpgIcJ4py3zIdZ'
    }
    r = requests.get(url = URL,headers=headers)
    print(r.text)
    s3_client = boto3.client('s3',region_name='us-east-1')
    
    s3_client.put_object(Body=r.text, Bucket='empjson123', Key='synopcharges.json')

    statement = "COPY INTO OUR_FIRST_DB.PUBLIC.employee_info FROM @OUR_FIRST_DB.PUBLIC.json_stage files = ('emp.json')"
    cursor.execute(statement)
  
     
process()