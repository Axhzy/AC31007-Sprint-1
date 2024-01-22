import json
import mysql.connector 

def lambda_handler(event, context):
    # TODO implement
    cnx = mysql.connector.connect(user='admin', password='Group3MasterPassword!',
                              host='bankdatabase.ct2cs466y605.us-east-1.rds.amazonaws.com',
                              database='BankDatabase')
    try:
       cursor = cnx.cursor()
       cursor.execute("""
          SELECT * FROM atm_data
       """) #test query
       result = cursor.fetchall()
    finally:
        cnx.close()
    return {
        'statusCode': 200,
        'body': json.dumps(result) #as a test returns all fields from database as json
    }


   


