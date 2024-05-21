# api/create_tutorial.py

import boto3
from datetime import datetime
import uuid

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('tutorials')

def create_tutorial(title, description, published):
    id = str(uuid.uuid4())
    created_at = datetime.utcnow().isoformat()
    updated_at = created_at

    item = {
        'id': id,
        'title': title,
        'description': description,
        'published': int(published),
        'createdAt': created_at,
        'updatedAt': updated_at
    }

    table.put_item(Item=item)
    return item
