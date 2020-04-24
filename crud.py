import pyodbc

def read(connection): #read query function
    print("Read")
    cursor = connection.cursor()
    #select all values from table named animal_list
    cursor.execute("select * from animal_list") 
    for row in cursor:
        print(f'row = {row}') 
    print()

def create(connection): #insert query function
    print("Create")
    cursor = connection.cursor()
    #insert values 89(int) and lion(char) into the animal_list table
    cursor.execute('insert into animal_list(id,animal) values(?,?);',(89, 'lion')) 
    connection.commit()
    read(connection) #calling read function to print newly inserted values

def update(connection): #update query function
    print("Update")
    cursor = connection.cursor()
    #update query with id = 89 as 'cat'
    cursor.execute('update animal_list set animal = ? where id = ?;',('cat', 89))
    connection.commit()
    read(connection) #calling read function to print newly inserted values


def delete(connection): #delete query function
    print("Delete")
    cursor = connection.cursor()
    #delete all values whose id is greater than 5
    cursor.execute('delete from animal_list where id > 5')
    connection.commit()
    read(connection) #calling read function to print newly inserted values

#creating a connection with SQL database
connection = pyodbc.connect('DRIVER=FreeTDS;SERVER=<IP_OR_HOSTNAME>;PORT=1433;DATABASE=<DATABASE_NAME>;UID=<USERNAME>;PWD=<PASSWORD>;TDS_Version=8.0;')
#eg - connection = pyodbc.connect('DRIVER=FreeTDS;SERVER=localhost;PORT=1433;DATABASE=TestDB;UID=SA;PWD=Mssql@2019;TDS_Version=8.0;')

read(connection)
create(connection)
update(connection)
delete(connection)

connection.close() #closing the connection with database
