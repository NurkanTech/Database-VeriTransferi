import mysql.connector
from datetime import datetime  
from db_demo import connection

#  Aşağıdaki örnek bilgiler için insert sorgusu oluşturup kayıtları ekleyelim
""" ("106","öztürk","topal",datetime(2003,2,10),"E"),
    ("107","leyla","elnajar",datetime(2008,1,17),"K"),
    ("108","hüseyin","aliyev",datetime(2011,6,7),"E"),
    ("109","aynura","meredov",datetime(2013,5,27),"K"),
    ("110","muhammed","hidayev",datetime(2004,5,10),"E")
"""
# ---->Plural Data Transfer to Database<-----

students=[
    ("106","öztürk","topal",datetime(2003,2,10),"E"),
    ("107","leyla","elnajar",datetime(2008,1,17),"K"),
    ("108","hüseyin","aliyev",datetime(2011,6,7),"E"),
    ("109","aynura","meredov",datetime(2013,5,27),"K"),
    ("110","muhammed","hidayev",datetime(2004,5,10),"E")
]

class Student:
    connect=connection
    mycursor=connect.cursor()
    def __init__(self,Student_Number,Name,Surname,Birthdate,Gender):
        self.Student_Number=Student_Number
        self.Name=Name
        self.Surname=Surname
        self.Birthdate=Birthdate
        self.Gender=Gender
    def saveStudent(self): # db'ye tekli veri girişi 
        sql="INSERT INTO Student(Student_Number,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value=(self.Student_Number,self.Name,self.Surname,self.Birthdate,self.Gender)
        Student.mycursor.execute(sql,value)
        try:
            Student.connection.commit() 
            print(f"{Student.mycursor.rowcount} tane kayit eklendi") # kayıt sayısı sorgusu
        except mysql.connector.Error as err:
            print("error",err)
        finally:
            Student.connection.close()       
    @staticmethod
    def saveStudents(students): # db'ye çoklu veri girişi 
        sql="INSERT INTO student(Student_Number,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values=students
        Student.mycursor.executemany(sql,values)
                
        try:
            Student.connection.commit() #ilgili veri bağlantı üzerinden db aktarır
            print(f"{Student.mycursor.rowcount} tane kayit eklendi") 
        except mysql.connector.Error as err:
            print("error",err)
        finally:
            Student.connection.close()

Student.saveStudents(students)    
