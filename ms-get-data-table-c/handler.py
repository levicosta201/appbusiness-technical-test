import json
import mysql.connector
import array
import boto3


def hello(event, context):

    clientDynamo = boto3.client(
        'dynamodb'
    )

    dynamodb = boto3.resource(
        'dynamodb'
    )

    data_base_exceptions = clientDynamo.exceptions
    response = dynamodb.Table('client_history').scan()

    body = {
        "message": "Dados encontrados com sucesso!",
        "dataResponse": response['Items'],
    }

    return body;
