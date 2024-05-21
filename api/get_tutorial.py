# api/get_tutorial.py

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('tutorials')

def get_tutorial(id):
    response = table.get_item(Key={'id': id})
    return response.get('Item')
