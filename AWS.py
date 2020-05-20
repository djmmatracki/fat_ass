import boto3
import json


def AddingAccount(nickname, email, password):

    client = boto3.client('lambda',
    aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
    region_name= "eu-west-1",
    aws_secret_access_key='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'
)

    response = client.invoke(
         FunctionName = "AccountAdd",
         InvocationType = "RequestResponse",
         Payload = json.dumps({"Nickname":nickname,"Password":password, "Email": email})
)
    response = json.loads(response['Payload'].read().decode("utf-8"))
    return response


def ifAccount(email, password):
    client = boto3.client('lambda',
    aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
    region_name= "eu-west-1",
    aws_secret_access_key='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'
)

    response = client.invoke(
        FunctionName="IfAccount",
        InvocationType="RequestResponse",
        Payload=json.dumps({"Password":password, "Email": email})
    )
    response = json.loads(response['Payload'].read().decode("utf-8"))
    print(response)
    return response
def getBasicInfo(ID):
    client = boto3.client('lambda',
    aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
    region_name="eu-west-1",
    aws_secret_access_key='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'
    )

    response = client.invoke(
        FunctionName="getBasicInfo",
        InvocationType="RequestResponse",
        Payload=json.dumps({"ID":ID})
    )
    response = json.loads(response['Payload'].read().decode("utf-8"))
    return response




