import psycopg2
import os
import ast
from bson.objectid import ObjectId
import networkx as nx
from collections  import Counter

class Exa_Task:

   def __init__(self):
       self.driver = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
       self.cur=self.driver.cursor()


   def close(self):
       self.driver.close()
       
   def creating(self):
       self.cur.execute("""CREATE TABLE Hashtag(
                             name text PRIMARY KEY,
                             tid text,
                             persons text,
                             
                         )""")
       self.cur.execute("""CREATE TABLE Person(
                             idd text PRIMARY KEY,
                             name text,
                             oid text,
                             fc text,
                             frc text,
                             foc text,
                             hlist text,
                         )""")
        
       self.driver.commit()
       
   def processing(self,tid='',person='',name='',oid='',text='',idd='',fc='',frc='',foc='',hlist='',n1='',n2='',icc=0,flag=0):
        if flag==0:
            insert_query = "INSERT INTO Hashtag VALUES {}".format("('"+name+"', '"+tid+"','"+person+"' )")
            self.cur.execute(insert_query)
        else:
            insert_query = "INSERT INTO Person VALUES {}".format("('"+idd+"', '"+name+"', '"+oid+"', '"+fc+"','"+frc+"','"+foc+"','"+hlist+"')")
            self.cur.execute(insert_query)
        
        self.driver.commit()
        
   def CURD(self,hashfull,perhash,listobj,hsashtid):
       print("----------------------------")
       tidhashdict=dict()
       ic=0
       for i in hsashtid:
           xli=[]
           print("Retriv Relation..... Step : "+str(ic))
           ic+=1
           for j in hsashtid:
               if i[0]==j[0]:
                   xli.append(j[1])
           tidhashdict[i[0]]=xli
       icc=0
       for i in hashfull:
           self.processing(name=str(i),tid=str(tidhashdict[i]),icc=icc,flag=1,person=str(perhash[i]))
           icc+=1 
       icc=0
       
       for i in listobj:
           self.processing(name=i[0],oid=i[1],text=i[2],idd=i[3],fc=i[4],frc=i[5],foc=i[6],hlist=str(i[7]),icc=icc,flag=0)
           icc+=1
       
          
   def read_data(self,filename="Tweets.txt"):
       dataset=[]
       ic=0
       with open(filename, "r",encoding="utf8") as f:
           while f.readline():
               d=f.readline()
               d=d.replace('ObjectId(','')
               d=d.replace('NumberLong(','')
               d=d.replace(')','')
               hashlist=[]
               d=ast.literal_eval(d)
               print("Load Data.....Line : "+str(ic))
               ic+=1
               for i in d['Entities']['Hashtag']:
                   hashlist.append(i['Text'].lower())
               dataset.append([
                                d['TwitterUserEntityModel']['ScreenName'],
                            str(d['_id']),
                            str(d['Text'].replace('\n',' ').replace('"',' ').replace("'",' ')),
                            str(d['TweetId']),
                            str(d['TwitterUserEntityModel']['_id']),
                            d['TwitterUserEntityModel']['FollowersCount'],
                            str(d['TwitterUserEntityModel']['FriendsCount']),
                            str(d['TwitterUserEntityModel']['FovouritesCount']),
                            hashlist
                            ])
       uniqlist=[]
       #Retril persons
       for i in dataset:
           uniqlist.append(i[0])
       setsnames=set(uniqlist)
       mergedlist=[]
       # merege all twwt of persons
       for i in setsnames:
           klist=[]
           for j in dataset:
               if i==j[0]:
                   klist.append(j)
           mergedlist.append(klist)
       
       listobj=[]
       reldict=dict()
       hashall=[]
       hsashtid=[]
       persons=dict()
       ic=0
       print("----------------------------------")
       for i in mergedlist:
           print("PreProcessing Data.....Step : "+str(ic))
           ic+=1
           lh=[]
           oh=[]
           kh=[]
           hashl=[]
           for j in i:
               lh.append(j[1])
               oh.append([j[2],j[3]])
               kh.append([j[-1],j[3]])
           for j in kh:
               for k in j[0]:
                   hashl.append(k)
                   hsashtid.append([k,j[1]])
           hashall.append(hashl)
           reldict[i[0][0]]=list(set(hashl))
           persons[i[0][0]]=i[0][5]
           listobj.append([i[0][0],str(lh),str(oh),i[0][4],str(i[0][5]),i[0][6],i[0][7],str(list(set(hashl)))])
       
       ic=0  
       hashfull=[]
       for i in hashall:
           for j in i:
               hashfull.append(j)
       hasht=list(Counter(hashfull))
       hashfull=list(set(hashfull))
       perhash=dict()
       for i in hashfull:
           plh=[]
           for j in reldict.keys():
               if i in reldict[j]:
                   plh.append(j)
           #print(i)
           perhash[i]=list(set(plh))
       
       # Database
       
       self.CURD(hashfull,perhash,listobj,hsashtid)
       hash10=[]
       hashfull10=[k for k, v in sorted(persons.items(), key=lambda item: item[1],reverse=True)]

       for i in hashfull10:
           hash10.append(reldict[i])
       hashfull10=[]
       for i in hash10:
           for j in i:
               hashfull10.append(j)
       res = [] 
       for i in hashfull10: 
           if i not in res: 
               res.append(i) 
       return hasht[:10],res[:10],hasht
#For Running
            
if __name__ == "__main__":
    exa = Exa_Task()
    ht,hf,hasht=exa.read_data()
    exa.close()       
  
