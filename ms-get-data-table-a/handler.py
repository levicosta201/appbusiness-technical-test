import json
import mysql.connector
import array


def hello(event, context):

    listResponse = []
    mydb = mysql.connector.connect(
        host="database-appbus.cbfi3acofhqb.us-west-2.rds.amazonaws.com",
        user="admin",
        password="elnata2022",
        database="appbus"
    )

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM database_a")
    myresult = mycursor.fetchall()

    body = {
        "message": "Dados encontrados com sucesso!",
        "dataResponse": myresult,
        "input": event,
    }

    response = body

    return response
