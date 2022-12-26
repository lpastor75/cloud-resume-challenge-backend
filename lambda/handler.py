import boto3
import os

client = boto3.client('dynamodb')
MY_DYNAMO_TABLE = os.environ['ENV_MYTABLE']

def lambda_handler(event, context):
    
    response = client.update_item(
        TableName = MY_DYNAMO_TABLE,
        Key = {
            'id': {'S': 'my_website'}
        },
        UpdateExpression = 'ADD visitors :inc',
        ExpressionAttributeValues = {':inc' : {'N': '1'}},
        ReturnValues = 'UPDATED_NEW'
        )
        
    value = response['Attributes']['visitors']['N']
    
    return {      
            'headers': {'Access-Control-Allow-Origin': '*'},
            'statusCode': 200,
            'body': {'visits':f'{value}'}
    }