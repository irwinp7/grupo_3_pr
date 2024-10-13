import pymysql

endpoint ='db-server-g3.c3cuoeyaoo1i.us-west-1.rds.amazonaws.com'
user = 'techg4ws'
passw = 'Tech3Cl0ud4W5'

def connectionSQL():
    try:
        pymysql.connect(
            host=endpoint,
            user=user,
            password = passw
            )
        print ("Succesfull connection to a database")
    except Exception as err:
        print("Error:" , err)

connectionSQL()