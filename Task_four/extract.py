import connector
from mysql.connector import Error


class DB_Extractor(object):

    def __init__(self, bd):
        self.bd = bd

    def execute_read_query(self, query):
        cursor = self.bd.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def print_subject(self):
        print("Subject:")
        subjects = self.execute_read_query("SELECT * from software_engineering.subject")
        for subject in subjects:
            print(subject)

    def print_teacher(self):
        teachers = self.execute_read_query("SELECT * from teacher_to_subject "
                                           "join subject s on teacher_to_subject.subjectName = s.id")
        for teacher in teachers:
            print(teacher)


if __name__ == '__main__':
    db = connector.DB_connector("127.0.0.1", "root", "", "software_engineering")
    connect = db.create_connection()
    connect.close()
    show = DB_Extractor(connect)
    show.print_subject()
    show.print_teacher()
