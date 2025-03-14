import json
import boto3   
from botocore.exceptions import ClientError

# Confirm email and region for the user pool
REGION="us-east-1"
USER_POOL_ID="us-east-1_KwhJunQsM"
CLIENT_ID="7j29g27ege8jt4aocrmo2r2oa3"

cognitoclient = boto3.client('cognito-idp', region_name=REGION)

# Function for            
def lambda_handler(event, context):
    username=event['body-json']['username']
    code=event['body-json']['code']
    result=False
    message=""
    response={}
    returndata={} 
    
    try:
        response = cognitoclient.confirm_sign_up(
                ClientId=CLIENT_ID,
                Username=username,
                ConfirmationCode=code
            )
        result=True
        message="User confirmed"
    except ClientError as e:
        message="Error in confirming email"
        if e.response['Error']['Code'] == 'UserNotFoundException':
            result=False
            message="Can't Find user by Email"
        elif e.response['Error']['Code'] == 'CodeMismatchException':
            result=False
            message="User Code Mismatch"
        elif e.response['Error']['Code'] == 'ParamValidationError':
            result=False
            message="Param Validation Error"
        elif e.response['Error']['Code'] == 'ExpiredCodeException':
            result=False
            message="Expired Code"
        elif e.response['Error']['Code'] == 'NotAuthorizedException':
            result=False
            message="User already confirmed"
        else:
            result=False
            message=e.response['Error']['Code']
    
    returndata['result']=result
    returndata['message']=message
    
    return {
        "statusCode": 200,
        "body": json.dumps(returndata)
    }
# Initial setup
# Email confirmation added
# Added error handling
# Morning update
# Evening fixes
# Added logging
# Security update
# Error handling
# Major refactor
# Bug fixes
# Performance tuning
# Project initialization
# API integration
# Error handling
