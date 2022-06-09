import json
import mysql.connector
from soupsieve import select
import sys
import re

class db:
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
            print(sql)
            print(value)

            mycursor = self.mydb.cursor()
            mycursor.execute(sql, value)
            self.mydb.commit()
      
      def edit(self, tableName , data= "", where=""  ):
            
            mycursor = self.mydb.cursor()

            sql = "UPDATE "+tableName+"  SET "+data+" WHERE "+where

            mycursor.execute(sql)

            self.mydb.commit()
      
      def changeFlagUser(self,chatId,number):
            self.edit("user","flag="+str(number),"id="+str(chatId))
      
      def addUserIfNotExist(self,chatId,name,userName):
            user = self.getInfo("user","id","id="+str(chatId))
            if user==[]:
                  self.setInfo("user",["id","name","userName","flag"],[str(chatId),str(name),str(userName),str(0)])
            # print(user)
      def getFlag(self,chatId):
            return self.getInfo("user","flag","id="+str(chatId))[0][0]
            
            
            

# t =Tools()
# id =t.getInfo("user",selector="id",where="id=1")
# t.setInfo("user",["id","name","userName","flag"],["2","ali","afds3",1])
# t.edit("user","id=10","id=1")
# t.changeFlagUser("10",0)
# t.addUserIfNotExist("27","java","javadkdf")
# print(t.getFlag("2"))
