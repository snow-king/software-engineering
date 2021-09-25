
import connector
from mysql.connector import Error


class DB_modify(object):

    def __init__(self, bd):
        self.bd = bd

    def execute_query(self, query):
        cursor = self.bd.cursor()
        try:
            cursor.execute(query)
            self.bd.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def append_subject(self, name, time, classroom ):
        insert = f"INSERT INTO software_engineering.subject(id, name, time, classroom) " \
                 f"values (4, '{name}', '{time}', '{classroom}')"
        self.execute_query(insert)

    def update_subject(self, name, time ):
        update = f"UPDATE software_engineering.subject set time ={time} where name ='{name}'"
        self.execute_query(update)

    def delete_subject(self, el):
        delete = f"DELETE FROM software_engineering.subject WHERE id = '{el}'"
        self.execute_query(delete)


if __name__ == '__main__':
    db = connector.DB_connector("127.0.0.1", "root", "", "software_engineering")
    connect = db.create_connection()
    show = DB_modify(connect)
    show.update_subject('Теория принятия решений', "1")
