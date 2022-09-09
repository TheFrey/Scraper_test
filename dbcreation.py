from mysql.connector import connect, Error


try:
    with connect(host='localhost',
                 user=input('Login: '),
                 password=input('Password: '),
                 database='test_task') as connection:
        # creating db
       # create_db_query = """CREATE DATABASE test_task"""
       # with connection.cursor() as cursor:
        #    cursor.execute(create_db_query)
        # creating table
        create_table = '''CREATE TABLE room_info(
                          title VARCHAR(100),
                          img VARCHAR(200),
                          pub_date VARCHAR(15),
                          city VARCHAR(20),
                          bedrooms VARCHAR(20),
                          description VARCHAR(500),
                          currency VARCHAR(5),
                          price DECIMAL(8, 2)
        )'''
        with connection.cursor() as cursor:
            cursor.execute(create_table)
except Error as e:
    print(e)


