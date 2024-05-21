# api/update_tutorial.py

import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('tutorials')

def update_tutorial(id, title=None, description=None, published=None):
    update_expression = []
    expression_attribute_values = {}
    
    if title:
        update_expression.append('title = :title')
        expression_attribute_values[':title'] = title
    if description:
        update_expression.append('description = :description')
        expression_attribute_values[':description'] = description
    if published is not None:
        update_expression.append('published = :published')
        expression_attribute_values[':published'] = int(published)
    
    if not update_expression:
        return None

    update_expression.append('updatedAt = :updatedAt')
    expression_attribute_values[':updatedAt'] = datetime.utcnow().isoformat()

    response = table.update_item(
        Key={'id': id},
        UpdateExpression='SET ' + ', '.join(update_expression),
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="ALL_NEW"
    )
    return response.get('Attributes')
