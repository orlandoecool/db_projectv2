from config.dbconfig import pg_config
import psycopg2

class RequestersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers natural inner join requesters;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterById(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers natural inner join requesters where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = cursor.fetchone()
        return result