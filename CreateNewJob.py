import psycopg2
import sys
import ast

__author__ = 'Owner'
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from CustomClassJson import encodeClassToJson
from CustomClassJson import decodeJsonToClass
from JobDescNode import JobDescNode
from Matcher import Matcher
from Scorer import Scorer
from Facade import Facade
from CustomClassJson import encodeClassToJson
from CustomClassJson import decodeJsonToClass
from ResumeProcessor import ResumeProcessor
import json

print("entering create new job")

contentID = sys.argv[2]
contentName = sys.argv[1]
print("got system variable")

with open("2.json", encoding='utf-8') as inFile:
    keyword = json.load(inFile)
    
keyword[0] =  keyword[0].replace("\f", " ")
if keyword[0]=="":
    keyword[0] = '-'
print("kee")
print(keyword[0])
with open("1.json", encoding='utf-8') as inFile:
    contentFile = json.load(inFile)
    
contentFile[0] =  contentFile[0].replace("\f", " ")

con = None
try:
    con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
    cur = con.cursor()
except psycopg2.DatabaseError as e:
    print ('Error %s' % e)
    sys.exit(1)
finally:
    if con:
        cur.execute("SELECT * FROM resume");
        rows = cur.fetchall()
        numRows = (len(rows))
        newJob = JobDescNode(contentID, contentFile, keyword)
        if (numRows == 0):
            ResumeProcessor.construct(newJob)
            toPrint = encodeClassToJson(newJob)
            cur.execute("INSERT INTO job VALUES (%s,%s,%s,%s)",(toPrint,'f', contentID ,contentName))
            con.commit()
            print('just store job')
        else:
            ResumeProcessor.construct(newJob)
            toPrint = encodeClassToJson(newJob)
            cur.execute("INSERT INTO job VALUES (%s,%s,%s,%s)",(toPrint,'f', contentID ,contentName))
            con.commit()
            f = Facade()
            matcher = Matcher(f)
            scorer = Scorer(f)
            cur.execute("SELECT isonce_resume FROM once")
            rows = cur.fetchall()
            for row in rows:
                if(row[0] is True):
                    cur.execute("UPDATE once SET isonce_resume=%s",('f',))
                    con.commit()
                    print('calling match 0 --1 ')
                    matcher.matchAll(0)
                    scorer.calculateScore()
                    print('calling match 0 --2')
                else:
                    matcher.matchAll(2)
                    scorer.calculateScore()
                    print('fdsfds')
            con.close()