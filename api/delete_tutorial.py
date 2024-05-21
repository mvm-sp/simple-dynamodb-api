# api/delete_tutorial.py

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('tutorials')

def delete_tutorial(id):
    response = table.delete_item(Key={'id': id})
    return response
