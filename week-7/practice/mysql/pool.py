# 2種方法 (隱式 or 顯式) > 連接池

# 1. mysql.connector.connect()
import mysql.connector
from mysql.connector import errors

try:
    # create connection pool and fetch the first connection
    db1=mysql.connector.connect(option_files='my.conf',
                                pool_name='my_connection_pool',
                                pool_size=3)
    print("Connection db1:", db1.connection_id)

    # fetch the second connection from the pool
    db2=mysql.connector.connect(pool_name='my_connection_pool')
    print("Connection db2:", db2.connection_id)

    # fetch the third connection from the pool
    db3=mysql.connector.connect(pool_name='my_connection_pool')
    print("Connection db3:", db3.connection_id)    

    try:
        # fetch the fourth connection from the pool
        db4=mysql.connector.connect(pool_name='my_connection_pool')

    except errors.PoolError as e:
        # connection pool exhausted, so we can't fetch 4th connection
        print(e)
        print('Closing db3 connection ')
        db3.close()

        # lets try fetching db4 again
        db4=mysql.connector.connect(pool_name='my_connection_pool')


except errors.Error as e:
    print(e)

else:
    print("Connection db1:", db1.connection_id)
    print("Connection db2:", db2.connection_id)
    print("Connection db4:", db4.connection_id)
    db1.close()
    db2.close()
    db4.close()


# 2. mysql.connector.pooling
'''
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errors

def query(sql):
    cursor= con_pool.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    cursor.close()
    return result
def off():
    con_pool.close()

try:

    # create the connection pool
    con_pool=MySQLConnectionPool(pool_name='my_connection_pool',
                                pool_size=3,
                                option_files='my.conf',)

    db1 = con_pool.get_connection()
    print("Connection db1:", db1.connection_id)
    
    # fetch the second connection from the pool
    db2 = con_pool.get_connection()
    print("Connection db2:", db2.connection_id)

    # fetch the third connection from the pool
    db3 = con_pool.get_connection()
    print("Connection db3:", db3.connection_id)

    try:
        # fetch the fourth connection from the pool
        db4 = con_pool.get_connection()

    except errors.PoolError as e:
        # connection pool exhausted, so we can't fetch 4th connection
        print(e)
        print('Closing db3 connection ')
        db3.close()

        # lets try fetching db4 again
        db4 = con_pool.get_connection()


except errors.Error as e:
    print(e)

finally:
    print("Connection db1:", db1.connection_id)
    print("Connection db2:", db2.connection_id)
    print("Connection db4:", db4.connection_id)
    db1.close()
    db2.close()
    db4.close()
'''
