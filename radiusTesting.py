#this is a version of the code in the api
#that we can use to test ideas for how to
#select atms in a given radius

import json
import mysql.connector

def getATMs(lat, long, radius): #takes in params (will be sent from website)
    cnx = mysql.connector.connect(user='admin', password='Group3MasterPassword!',               #login to database
                              host='bankdatabase.ct2cs466y605.us-east-1.rds.amazonaws.com',
                              database='BankDatabase')
    try:
    cursor = cnx.cursor()
    cursor.execute("""
        SELECT * FROM atm_data






        
    """)                             #SQL here, currently just gets all rows
    result = cursor.fetchall()
    print (result)                   #print result (will return back to website)
    finally:
        cnx.close()