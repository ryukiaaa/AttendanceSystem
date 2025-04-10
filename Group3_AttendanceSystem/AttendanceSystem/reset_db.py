import mysql.connector

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='dblapuredemo123'
    )
    
    cursor = conn.cursor()
    
    # Drop the database if it exists
    cursor.execute('DROP DATABASE IF EXISTS attendancesystem')
    
    # Create a new database
    cursor.execute('CREATE DATABASE attendancesystem')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print('Database reset successfully')
    
except mysql.connector.Error as err:
    print(f"Error: {err}")