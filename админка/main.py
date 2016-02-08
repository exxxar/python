from configparser import ConfigParser
import MySQLdb
import os



class SQL
    db = None
    
    PATH = dbfiles
    
    def read_db_config(self,filename='db.ini', section='mysql')
        try
            parser = ConfigParser()           
            parser.read(filename)           

            # get section, default to mysql
            params = {}
            if parser.has_section(section)
                items = parser.items(section)
                for item in items
                    params[item[0]] = item[1]
            else
                raise Exception('{0} not found in the {1} file'.format(section, filename))
            return params
        except Exception as e
            print e
        return 0
    
    def init(self)
        self.connect()
        param = self.read_db_config()
        try
            sql = 'CREATE DATABASE '+param['database']
            cur = self.db.cursor().execute(sql)
            print cur            
        except Exception as e
            print Error in creating db [+str(e)+]
            
        try
            os.mkdir(self.PATH)
        except OSError as e
            print e
            
        for i in os.listdir(self.PATH)
            if (i.find(.sql)!=-1)
                f = open(self.PATH++i)
                sql = 
                for k in f.readlines()
                    sql+=k                    
                print sql
                try  
                    cur = self.db.cursor().execute(sql)
                    print cur
                except Exception as e
                    print Error in creating table [+str(e)+]
                    
        self.close()
        return 0
    
    def dropTables(self)
        self.connect()
        try
            sql = DROP TABLE items              
            cur = self.db.cursor().execute(sql)
            print cur
        except Exception as e
            print Error in DROP table [+str(e)+]
        
        try
            sql = DROP TABLE itemType              
            cur = self.db.cursor().execute(sql)
            print cur
        except Exception as e
            print Error in DROP table [+str(e)+]
        self.close()
        return 0    
    
    def connect(self)
        param = self.read_db_config() 
        
        self.db = MySQLdb.connect(host=param['host'],    # your host, usually localhost
                            user=param['user'],         # your username
                            passwd=param['password'],  # your password
                            db=param['database'])        # name of the data base
        #for row in cur.fetchall()
           # print row[0]
        return 0

    def doSQL(self,sqlText)
        try
            self.connect()

            cur = self.db.cursor()
            cur.execute(sqlText)

            self.close()
            return cur
        except Error as e
            print e
            self.close()
        return 0
    
    def insert(self)
        sql = INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        return 0
    
    def close(self)
        self.db.close()        
        return 0
    
a = SQL()
a.init()
a.doSQL(SELECT  FROM tab)