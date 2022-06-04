import math
import sys
class Similarities:
      frequently_list = {}
      length_Doc = 0
      documents = []
      idf_list = {}
      
      def __init__(self,listOfDoc):
            for doc in listOfDoc:
                  self.addDocument(doc)
                  
            self.createIdfList()
            
      
      def addDocument(self , document):
            #create list of words 
            listOfDoc =  document.split(' ')
            listOfFrequency = {}
            
            for word in listOfDoc:
                  listOfFrequency[word] = listOfFrequency.get(word,0)+1
                  self.frequently_list[word] = self.frequently_list.get(word, 0) + 1

            self.tf_list = listOfDoc
            
            #increase number of document        
            self.length_Doc = self.length_Doc + 1
            # add information to list     
            self.documents.append(["d"+str (self.length_Doc), listOfFrequency])
      
      def createIdfList(self):
            for word in self.frequently_list:
                  repeat = self.numberRepeatInDocs(word)
                  self.idf_list[word] = math.log2(self.length_Doc/repeat)
      
      def createTfList(self):
            
            for list in self.documents:
                  key = list[0]
                  words = list[1]
                  
                        
                        
                  
      
      def numberRepeatInDocs(self ,word):
            number = 0
            for list in self.documents:
                  words = list[1]
                  if word in words:
                        number = number + 1
            return number
            
            

s =  Similarities()
s.addDocument("new york times")
s.addDocument("new york post")
s.addDocument("los angeles times")
s.createTfList()
print(s.idf_list)


