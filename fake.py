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



s = list()
con = None
try:
    con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
    cur = con.cursor()
except psycopg2.DatabaseError as e:
    print ('Error %s' % e)
    sys.exit(1)
finally:
    if con:
        cur.execute("SELECT resume_data::text FROM resume WHERE resume_isprocessed = %s",('f'));
        rows = cur.fetchall()
        for row in rows:
            pp = str(row[0])
            print(pp)
            s.append(decodeJsonToClass(pp))
        cur.execute("UPDATE resume SET resume_isprocessed=%s",('t'));
        con.commit()
    con.close()