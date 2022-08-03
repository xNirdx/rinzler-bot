import mysql.connector
import configparser


class DB:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.database = mysql.connector.connect(
            host=self.config['DATABASE']['host'],
            user=self.config['DATABASE']['user'],
            password=self.config['DATABASE']['password'],
            database=self.config['DATABASE']['database']
        )

        self.cursor = self.database.cursor()

    async def add_role(self):
        sql = "INSERT INTO roles VALUES (69, 420)"

        self.cursor.execute(sql)
        self.database.commit()
