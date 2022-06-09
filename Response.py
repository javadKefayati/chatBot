from Similarities import Similarities
import random
import json
import  sys



class Response:
      questionData = {}
      answerData = {}
      listOfData = []
      
      def __init__(self , dataQ,dataA):
            self.questionData = dataQ
            self.answerData = dataA
            
            
      def createListOfDataWithoutKey(self):
            for d in self.questionData:
                  self.listOfData+=self.questionData[d]
            return self.listOfData
      
      def checkGroup(self, query):
            sim = Similarities()
            sim.initClass(self.listOfData)
            sim.setQuery(query)
            namSimilarities , valueSimilarities = sim.result()
            print(namSimilarities)
            for d in self.questionData:
                  nL = self.questionData[d]
                  for n in nL:
                      if n == namSimilarities:
                            return d
      
      def getResponse(self,query):
            group = self.checkGroup(query)
            
            for a in self.answerData:
                  if a == group:
                        nList = self.answerData[a]
                        randIndex = random.randint(0, len(nList)-1)
                        print( nList[randIndex])
                        
                  
            
      
                  
                  


with open("question.json", "r") as file:
    dataQ = json.load(file)
    
with open("answer.json", "r") as file:
    dataA = json.load(file)

r =Response(dataQ,dataA)
sim = Similarities()
print(r.createListOfDataWithoutKey())
r.getResponse("خداحافظ")

