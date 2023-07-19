import mysql.connector
import csv
workbook_file=open('quiz_sheet.csv','r')
workbook_reader=csv.reader(workbook_file)
L=[]
for row in workbook_reader:
    L.append(tuple(row))
workbook_file.close()

#print(L)

db_connection = mysql.connector.connect(
host= "localhost",
user= "root",
passwd= ""
)

db_cursor = db_connection.cursor()

db_cursor.execute("DROP DATABASE IF EXISTS QuizDB2")

db_cursor.execute("CREATE DATABASE QuizDB2")

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="QuizDB2"
)
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE quiz (No INT  AUTO_INCREMENT PRIMARY KEY, Question CHAR(255) NOT NULL, option1 CHAR(100), option2 CHAR(100), option3  CHAR(100), option4 CHAR(100), answer CHAR(100))")
db_cursor.execute("CREATE TABLE users (No INT AUTO_INCREMENT PRIMARY KEY,FistName CHAR(255) NOT NULL, LastName CHAR(255) NOT NULL,username CHAR(255) NOT NULL, password CHAR(100), usertype CHAR(100),status CHAR(10))")
db_cursor.execute("CREATE TABLE User_score(No INT AUTO_INCREMENT PRIMARY KEY, username CHAR(255) NOT NULL, score int(3), usertype CHAR(100))")

sql_quiz= "INSERT INTO quiz(Question, option1, option2, option3, option4, answer) VALUES(%s,%s,%s,%s,%s,%s)"
db_cursor.executemany(sql_quiz,L)

sql_users= "INSERT INTO users(FistName,LastName,username,password,usertype,status) VALUES('AP','Group 07','Admin','123','ADMIN','INACTIVE')"
db_cursor.execute(sql_users)
db_connection.commit()


db_connection.close()

