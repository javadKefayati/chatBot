import json
import mysql.connector
from soupsieve import select
import sys
import re

class Tools:
      mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="", 
                  database="ai"
                        )                 
       
      def getInfo(self,tableName,selector =" ",where=""):
            mycursor = self.mydb.cursor()
            if where=="":
                  mycursor.execute("SELECT "+selector+" FROM "+tableName)
            else:
                   mycursor.execute("SELECT "+selector+" FROM "+tableName+" WHERE "+where )
                  
            myresult = mycursor.fetchall()
            return myresult
      
      def setInfo(self,tableName,columns=[],value=[]):
            col =""
            for v in range(0,len(value)):
                  
                  if len(value)-1 != v:
                        col +=" "+columns[v]+" , "
                  else :
                        col += ""+columns[v]+" "
            
            valStr =""
            for v in range(0,len(value)):
                  
                  if len(value)-1 != v:
                        valStr +=" %s , "
                  else :
                        valStr += " %s "
                  
            sql = "INSERT INTO "+tableName+" ( "+col+ ") VALUES ( "+valStr+" )"

            mycursor = self.mydb.cursor()
            mycursor.execute(sql, value)
            self.mydb.commit()
      
      def edit():
            

t =Tools()
# id =t.getInfo("user",selector="id",where="id=1")
# t.setInfo("user",["id","name","userName","flag"],["2","ali","afds3",1])
