import pymysql

#获取连接方法

class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '',
            db = 'test',
            charset = 'utf8'
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()


#封装数据库查询操作
    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exe_c(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

#封装常用数据库操作
    def check_user(self,name):
        result = self.query("select * from user where name='{}'".format(name))
        return True if result else False


    def add_user(self,name,password):
        sql = "insert into user (name,password) value ('{}','{}')".format(name,password)
        self.exe_c(sql)

    def del_user(self, name):
        self.exe_c("delete from user where name='{}'".format(name))



