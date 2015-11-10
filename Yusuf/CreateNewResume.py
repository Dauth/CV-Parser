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
#http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
#http://stackoverflow.com/questions/20823665/python-syntaxerror-invalid-syntax-for-elif-lenorg-1

name = sys.argv[1]
hpNumber = sys.argv[2]
email = sys.argv[3]
contentName = sys.argv[4]
content = sys.argv[5]
# content = content.replace('[ ', '["')
# content = content.replace(']', '"]')

with open("1.json", encoding='utf-8') as inFile:
    contentFile = json.load(inFile)

newResume = ResumeNode(name, hpNumber, email, contentName, contentFile)
con = None
try:
        con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
        cur = con.cursor()
except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)
finally:
        if con:
            cur.execute("SELECT * FROM job");
            rows = cur.fetchall()
            numRows = (len(rows))

            if (numRows == 0):
                ResumeProcessor.construct(newResume)
                toPrint = encodeClassToJson(newResume)
                #print(type(newResume.getContent()))
                print(toPrint)
                cur.execute("INSERT INTO resume VALUES (%s,%s,%s,%s,%s,%s)",(toPrint,'f',contentName,name,hpNumber,email))
                con.commit()
            else:
                ResumeProcessor.construct(newResume)
                toPrint = encodeClassToJson(newResume)
                #print(type(newResume.getContent()))
                print(toPrint)
                cur.execute("INSERT INTO resume VALUES (%s,%s,%s,%s,%s,%s)",(toPrint,'f',contentName,name,hpNumber,email))
                con.commit()
                f = Facade()
                matcher = Matcher(f)
                scorer = Scorer(f)
                cur.execute("SELECT isonce_resume FROM once")
                rows = cur.fetchall()
                for row in rows:
                    if(row[0]=='t'):
                        matcher.matchAll(0)
                        scorer.calculateScore()
                    else:
                        cur.execute("UPDATE once SET isonce_resume=%s",('f'));
                        matcher.matchAll(1)
                        scorer.calculateScore()
            con.close()

