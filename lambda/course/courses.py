import boto3
import os
import json
dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def meta_info(event,context):

    try:
        std_resp = table.scan(
            AttributesToGet=[
                'course_id',
                'course_img',
                'course_name',
                'types',
                'mode',
                'cc'
            ]
        )
        resp = {
            'body': std_resp['Items'],
            'message': 'Success',
            'statusCode':200
        }
        return resp
    except Exception as e:
        resp = {
            'message': 'Error fetching courses',
            'statusCode': 500
        }
        raise Exception(json.dumps(resp))

def add(event,context):
    return "Not yet implemented"
