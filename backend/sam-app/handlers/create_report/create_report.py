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
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'statusCode': 200,
        'body': json.dumps({'executionArn': response['executionArn']})
    }
