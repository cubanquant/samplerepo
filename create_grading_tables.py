import sqlite3

DROP_STUDENT_TABLE = "DROP TABLE IF EXISTS Students;"
DROP_QUIZZES_TABLE = "DROP TABLE IF EXISTS Quizzes;"
DROP_RESULTS_TABLE = "DROP TABLE IF EXISTS Results;"

STUDENTS_TBL = """
CREATE TABLE IF NOT EXISTS Students(
    student_id integer PRIMARY KEY AUTOINCREMENT ,
    first TEXT,
    last TEXT
)
"""

QUIZZES_TBL = """
CREATE TABLE IF NOT EXISTS Quizzes(
    quiz_id integer PRIMARY KEY AUTOINCREMENT ,
    subject TEXT,
    questions integer,
    quiz_date TEXT
)
"""

QUIZ_RESULTS_TBL = """
CREATE TABLE IF NOT EXISTS Results(
    student_id integer,
    quiz_id integer,
    score integer
)
"""


def create_tables():
    conn = sqlite3.connect('grades.db')  # connect to the database

    cur = conn.cursor()

    cur.execute(DROP_QUIZZES_TABLE)
    cur.execute(DROP_RESULTS_TABLE)
    cur.execute(DROP_STUDENT_TABLE)

    cur.execute(STUDENTS_TBL)
    cur.execute(QUIZZES_TBL)
    cur.execute(QUIZ_RESULTS_TBL)
    conn.commit()

    conn.close()


if __name__ == "__main__":
    create_tables()

