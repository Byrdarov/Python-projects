def get_uoms(connection):
    cursor=connection.cursor()
    query=("SELECT * from uom")
    cursor.execute(query)

    response=[]
    for(uom_id,uom_name) in cursor:
        response.append({
            'uom_id':uom_id,
            'uom_name':uom_name
        })
    return response




if __name__=="__main__":
    from sql_conncetion import get_sql_conncetion
    connection=get_sql_conncetion()
    print(get_uoms(connection))