import json
import boto3

def lambda_handler(event, context):
    state_machine_arn = 'STATE_MACHINE_ARN'
    
    # Start the state machine execution
    client = boto3.client('stepfunctions')
    input_data = {
    }
    
    response = client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )

    return {
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Requested-With',
            'Access-Control-Allow-Origin': 'https://main.d5yg8u5ydak1.amplifyapp.com',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
            'Access-Control-Allow-Credentials': 'true'
        },
        'statusCode': 200,
        'body': json.dumps({'executionArn': response['executionArn']})
    }
