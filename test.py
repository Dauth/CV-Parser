import psycopg2
import sys

#http://stackoverflow.com/questions/12906351/importerror-no-module-named-psycopg2
#http://stackoverflow.com/questions/28228241/how-to-connect-to-a-remote-postgresql-database-with-python

con = None

try:
	con = psycopg2.connect(database='d1s3idai1l2u3d', user='ymqkpiilrdlhvu', password='lrt8l-hFcKfcZ3FYgM79Ek45y6', host='ec2-54-197-241-24.compute-1.amazonaws.com', port='5432', sslmode='require')
	cur = con.cursor()
	cur.execute('SELECT version()')
	ver = cur.fetchone()
	print ver    
except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
	cur.execute("SELECT firstextract_id FROM firstextract WHERE firstextract_isprocessed = %s",('f'));
	rows = cur.fetchall()
	for row in rows:
		decodeJsonToClass();
		print row
        con.close()
