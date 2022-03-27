import psycopg2


class Connection:
    def __init__(self, dbname, user, passwd, host, port=5432):
        self.__connection = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=passwd,
            port=port
        )

    def get(self):
        return self.__connetion
