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

    async def add_role(self, role, group_id):
        sql = f"INSERT INTO roles VALUES ({role.id}, {group_id})"

        self.cursor.execute(sql)
        self.database.commit()

    def get_role_groups(self):
        sql = "SELECT * FROM role_groups"

        self.cursor.execute(sql)

        role_groups = self.cursor.fetchall()

        return role_groups
