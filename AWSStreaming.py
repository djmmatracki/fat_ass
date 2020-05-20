import boto3
import json


def getFile(ID):
    x = open("logs.txt","w")

    client = boto3.client('lambda',
        aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
        region_name="eu-west-1",
        aws_secret_access_key='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')

    response = client.invoke(
        FunctionName="getFile",
        InvocationType="RequestResponse",
        Payload=json.dumps({"ID": ID})

    )
    response = json.loads(response['Payload'].read().decode("utf-8"))

    temp = response["AudioURL"]
    x = list(temp)
    x.pop(4)
    response["AudioURL"] = "".join(x)

    temp = response["ImageURL"]
    x = list(temp)
    x.pop(4)
    response["ImageURL"] = "".join(x)

    return response

def uploadFile(file,Image,author,hashtags):
    s3 = boto3.resource('s3',
                        aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
                        region_name="eu-west-1",
                        aws_secret_access_key='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'
                        )

    FileName = file.split("/")[-1]
    ImageName = Image.split("/")[-1]

    client = boto3.client('lambda',
                          aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
                          region_name="eu-west-1",
                          aws_secret_access_key='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'
                          )

    response = client.invoke(
        FunctionName="UploadingFiles",
        InvocationType="RequestResponse",
        Payload=json.dumps({"Name": FileName})
    )
    client = boto3.client('s3',
                          aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
                          region_name="eu-west-1",
                          aws_secret_access_key='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'
                          )

    response = json.loads(response['Payload'].read().decode("utf-8"))

    Info = json.dumps({"Author": author, "ImageName": ImageName, "Hashtags": hashtags})

    s3.meta.client.upload_file(file, 'beatshouse', response["Directory"] + FileName,
                               ExtraArgs={'ContentType': 'audio/mpeg'})
    s3.meta.client.upload_file(Image, 'beatshouse', response["Directory"] + "Image.png",
                               ExtraArgs={'ContentType': 'image/png'})
    client.put_object(Body=Info, Bucket='beatshouse', Key=response["Directory"] + "Info.json",
                      ContentType='text/plain', )


    print("Done")

def getRandomList(number):
    client = boto3.client('lambda',
        aws_access_key_id='AKIA6L3D7G5EQN7DTZHZ',
        region_name="eu-west-1",
        aws_secret_access_key='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'
                          )


    response = client.invoke(
        FunctionName="getRandomList",
        InvocationType="RequestResponse",
        Payload=json.dumps({"Number":number})
    )
    response = json.loads(response['Payload'].read().decode("utf-8"))
    return response