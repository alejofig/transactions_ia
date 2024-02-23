import urllib.parse
import boto3
from openai import OpenAI
import os
from constants import prompt
import json
import requests

client = OpenAI()

s3 = boto3.client('s3')
def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        obj = response['Body'].read().decode("utf-8")
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{obj} {prompt} "}
            ]
            )
        requests.post(os.getenv("ZAPIER_HOOK"), data=json.loads(completion.choices[0].message.content))
        #createPage(os.getenv("TOKEN_NOTION"), os.getenv("DATABASE_ID_NOTION"),vals)
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
