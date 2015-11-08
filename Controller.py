import psycopg2
import sys
import ast

__author__ = 'Owner'
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from Matcher import Matcher
from Scorer import Scorer
from Facade import Facade
from CustomClassJson import encodeClassToJson
from CustomClassJson import decodeJsonToClass
from ResumeProcessor import ResumeProcessor
#http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
#http://stackoverflow.com/questions/20823665/python-syntaxerror-invalid-syntax-for-elif-lenorg-1

class Controller(object):

    def createNewResume(self, name, hpNumber, email, contentName, content):
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
                newResume = ResumeNode(name, hpNumber, email, contentName, content)
                
                if (numRows == 0):
                    ResumeProcessor.construct(newResume)
                    toPrint = encodeClassToJson(newResume)
                    cur.execute("INSERT INTO resume VALUES (%s,%s,%s,%s,%s,%s)",(toPrint,'f',contentName,name,hpNumber,email))
                    con.commit()
                else:
                    ResumeProcessor.construct(newResume)
                    toPrint = encodeClassToJson(newResume)
                    cur.execute("INSERT INTO resume VALUES (%s,%s,%s,%s,%s,%s)",(toPrint,'f',contentName,name,hpNumber,email))
                    con.commit()
                    f = Facade()
                    matcher = Matcher(f)
                    scorer = Scorer(f)
                    matcher.matchAll(1)
                    scorer.calculateScore()
                con.close()
                
    def createNewJob(self, contentName, contentID, keyword, content):
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
                newJob = JobDescNode(contentID, keyword, content)
                if (numRows == 0):
                    ResumeProcessor.construct(newJob)
                    toPrint = encodeClassToJson(newJob)
                    cur.execute("INSERT INTO job VALUES (%s,%s,%s,%s)",(toPrint,'f', contentID ,contentName))
                    con.commit()
                else:
                    ResumeProcessor.construct(newJob)
                    toPrint = encodeClassToJson(newJob)
                    cur.execute("INSERT INTO job VALUES (%s,%s,%s,%s)",(toPrint,'f', contentID ,contentName))
                    con.commit()
                    f = Facade()
                    matcher = Matcher(f)
                    scorer = Scorer(f)
                    matcher.matchAll(2)
                    scorer.calculateScore()
                con.close()
