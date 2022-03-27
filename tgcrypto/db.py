import psycopg2

class DataBase:
    def __init__(self, host, database, user, password):
        self.__host=host
        self.__database=database
        self.__user=user
        self.__password=password

    def connect(self):
        print(f"Connect to {database}")
        self.__conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
            )
        def test():
            cur = self.__conn.cursor()
            cur.execute("SELECT version()")
            ver = cur.fetchone()
            print(ver)
            cur.close()
        print("Start test")
        test()


