class Similarities:
      tf_list ={}
      length_Doc = 0
      
      def addDocument(self , document):
            #create list of words 
            listOfDoc =  document.split(' ')
            listOfFrequency = {}
            
            for word in listOfDoc:
                  listOfFrequency[word] = listOfFrequency.get(word,0)+1
            
            self.tf_list = listOfDoc
            
            #increase number of document        
            self.length_Doc = self.length_Doc + 1
      
      def createIdfList():
            
            
            
            

s =  Similarities()
s.addDocument("hello every one one one")
