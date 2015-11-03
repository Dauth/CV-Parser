
import ResumeNode
import JobDescNode
from CustomClassJson import decodeJsonToClass
from CustomClassJson import encodeClassToJson
import psycopg2
import sys
import ast
import json

class Facade(object):
    db = None
    count = 0

    def getNewResumes(self):
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
                cur.execute("SELECT resume_data FROM resume WHERE resume_isprocessed = %s",('f'));
                rows = cur.fetchall()
                for row in rows:
                    pp = str(row[0]).replace("u'", '"')
                    pp = pp.replace("'", '"')
                    pp = pp.replace('\\n', ' ')
                    pp = pp.replace('\\', ' ')
                    s.append(decodeJsonToClass(pp))
            con.close()
            return s

    def getAllResumes(self):
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
                cur.execute("SELECT resume_data FROM resume");
                rows = cur.fetchall()
                for row in rows:
                    pp = str(row[0]).replace("u'", '"')
                    pp = pp.replace("'", '"')
                    pp = pp.replace('\\n', ' ')
                    pp = pp.replace('\\', ' ')
                    s.append(decodeJsonToClass(pp))
            con.close()
            return s

    def getNewJobs(self):
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
                cur.execute("SELECT job_data FROM job WHERE job_isprocessed = %s",('f'));
                rows = cur.fetchall()
                for row in rows:
                    pp = str(row[0]).replace("u'", '"')
                    pp = pp.replace("'", '"')
                    pp = pp.replace('\\n', ' ')
                    pp = pp.replace('\\', ' ')
                    s.append(decodeJsonToClass(pp))
            con.close()
            return s

    def getAllJobs(self):
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
                cur.execute("SELECT job_data FROM job");
                rows = cur.fetchall()
                for row in rows:
                    pp = str(row[0]).replace("u'", '"')
                    pp = pp.replace("'", '"')
                    pp = pp.replace('\\n', ' ')
                    pp = pp.replace('\\', ' ')
                    s.append(decodeJsonToClass(pp))
            con.close()
            return s

    def getMatchBoxes(self):
        s = set()
        con = None
        try:
                con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
                cur = con.cursor()
        except psycopg2.DatabaseError as e:
                        print ('Error %s' % e)
                        sys.exit(1)
        finally:
                if con:
                        cur.execute("SELECT matchbox_data FROM matchbox");
                        rows = cur.fetchall()
                        for row in rows:
                                pp = str(row[0]).replace("u'", '"')
                                pp = pp.replace("'", '"')
                                pp = pp.replace('\\n', ' ')
                                pp = pp.replace('\\', ' ')
                                s.add(decodeJsonToClass(pp))
                con.close()
                return s

    def storeMatchBoxes(self,mboxes):
        con = None
        try:
            con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
            cur = con.cursor()
        except psycopg2.DatabaseError as e:
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            for xx in mboxes:
                toPrintTwo = encodeClassToJson(xx)
                #http://stackoverflow.com/questions/19365072/postgresql-typeerror-not-all-arguments-converted-during-string-formatting
                cur.execute("INSERT INTO matchbox VALUES (%s)",(toPrintTwo,))
                con.commit()
            con.close()

    def storeResults(self,result):
        con = None
        try:
            con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
            cur = con.cursor()
        except psycopg2.DatabaseError as e:
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            cur.execute("INSERT INTO resulttwo VALUES (%s)",(json.dumps(result),))
            con.commit()
            con.close()
