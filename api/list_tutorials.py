# api/list_tutorials.py

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('tutorials')

def list_tutorials():
    response = table.scan()
    return response.get('Items', [])
