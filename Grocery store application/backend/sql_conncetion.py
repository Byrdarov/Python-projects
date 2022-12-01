import mysql.connector
__cnx=None
def get_sql_conncetion():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='wtf1234567890',
                                      host='127.0.0.1',
                                      database='store_store')
    return __cnx