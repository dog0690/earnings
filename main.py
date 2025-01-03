import os
import mysql.connector
import time
import datetime
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def clock():
    while True:
        now = datetime.datetime.now()
        start_time = datetime.time(9, 30)
        end_time = datetime.time(16, 00)
        current_time = now.time().replace(microsecond=0)
        if end_time >= now.time() >= start_time:
            main()
        print(current_time)
        time.sleep(5)
        clear_terminal()
def main():
    print("hello world")
db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database = 'stocks'
)
mycursor = db.cursor()
clock()