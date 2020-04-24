# MSSQL_pyodbc
I was trying to connect MSSQL with python using pyodbc on my Linux system and had trouble to find a guide that was put together with upto date instructions. So here it is. 

Step 1 : 
Install MSSQL SERVER your linux machine using - 
https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15

ps - follow the optional instructions too!

Step 2 : 
Install freeTDS, pyodbc and sqlalchemy - 
	sudo apt-get install freetds-dev freetds-bin unixodbc-dev tdsodbc
	pip install pyodbc sqlalchemy

Step 3 : 
Change your odbcinst.ini file in your /etc folder -
-Create a odbcinst.ini file in your text editor and save it anywhere other than /etc. It should look something like this - 
[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
Setup=/usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
Count =
Usuage = 1
-Open terminal in /etc and use the command -
sudo rm odbcinst.ini
-Open terminal in the folder where u stored newly created odbcinst.ini file and use the command -
sudo mv odbcinst.ini /etc

Step 4 :
Run the python program!


