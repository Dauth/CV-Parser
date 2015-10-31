import psycopg2
import sys
import ast

__author__ = 'Owner'
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from CustomClassJson import encodeClassToJson
from CustomClassJson import decodeJsonToClass
    
newResume = ResumeNode(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
toPrint = encodeClassToJson(newResume)
print toPrint
con = None
try:
    con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
    cur = con.cursor()
except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
finally:
    if con:
        cur.execute("INSERT INTO resume VALUES (%s,%s,%s,%s,%s,%s)",(toPrint,'f',sys.argv[4],sys.argv[1],sys.argv[2],sys.argv[3]))
        con.commit()
        con.close()