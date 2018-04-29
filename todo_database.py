import pymysql

def db_check_remove(id):

    sql = "DELETE  FROM task WHERE id=%s" # define DB query

    conn = pymysql.connect(user='root',password='',database='lab5_flask', host='localhost')  # create a connection with all connection parameters to open a connection

    cursor = conn.cursor()  # from the connection we create a cursor
    cursor.execute(sql,(id,))  # from the cursor we execute the query; execute takes 2 arguments: 1. query template and 2. a tuple to be substituted in the query (it will replace %s in the query with 'username')
    conn.commit()
    conn.close()  # always remember to close the connection before returning

    return   # if there is no user in the database the function will return NULL otherwise it returns all the user known data

def showTask():

    sql = "SELECT id, todo FROM task"

    conn = pymysql.connect(user='root',password='Petronilla11.',database='lab5_flask', host='localhost')  # create a connection with all connection parameters to open a connection

    cursor = conn.cursor()  # from the connection we create a cursor
    cursor.execute(sql)  # from the cursor we execute the query; execute takes 2 arguments: 1. query template and 2. a tuple to be substituted in the query (it will replace %s in the query with 'username')
    result = cursor.fetchall()  # actually from the DB we need to fetch one result only since either we have a result (username found in the DB) or no result; if there is a result this will be the full data about the user. If it is non present, then 'result' will be NULL
    cursor.close()
    conn.close()  # always remember to close the connection before returning

    return result  # if there is no user in the database the function will return NULL otherwise it returns all the user known data

def new_Task(todo): # insert new task into the DB ( if it is not already present )

    sql = "SELECT id, todo FROM task WHERE todo=%s"  # define DB query

    conn = pymysql.connect(user='root', password='Petronilla11.', database='lab5_flask', host='localhost')  # create a connection with all connection parameters to open a connection

    cursor = conn.cursor()  # from the connection we create a cursor

    cursor.execute(sql,(todo,)) # execute search query

    result = cursor.fetchone()
    cursor.close()

    if result!=None:
        print("The Task is already present within the DataBase")

    else:
        sql_insert = "INSERT INTO task (todo) VALUES (%s)"  # insertion query
        cursor = conn.cursor()
        cursor.execute(sql_insert,(todo,))
        conn.commit()  # commite to DB
        cursor.close() # close cursor

    conn.close()   # close connection
    return

if __name__=='__main__':

    print(showTask())

    new_Task('go to sleep')

    #db_check_remove()  # valid user