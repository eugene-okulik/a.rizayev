import random

import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()


def insert_subject(subj_name, cur):
    cur.execute("INSERT INTO subjects (title) VALUES (%s)", (subj_name,))
    return cur.lastrowid


def insert_lesson(lesson_name, subject_id, cur):
    cur.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (lesson_name, subject_id))
    return cur.lastrowid


books = ('4 mushketera', '5 mushketera')
subjects = ('Chemistry_2', 'Geography_2', 'Physics_2')
lessons = ('Урок 03', 'Урок 04')

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Gena', 'Bukin5')")
student_id = cursor.lastrowid
cursor.execute("INSERT INTO `groups` (title, start_date, end_date)"
               " VALUES ('Schastlivy vmeste 6', 'Apr 2005', 'May 2010')")
group_id = cursor.lastrowid
query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query, (group_id, student_id))

books_tuples = [(book, student_id) for book in books]
cursor.executemany("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", books_tuples)

subject_ids = []
for subject in subjects:
    subject_ids.append(insert_subject(subject, cursor))

lesson_ids = []
for subject_id in subject_ids:
    for lesson in lessons:
        lesson_ids.append(insert_lesson(lesson, subject_id, cursor))

vals = [(str(random.randint(1, 100)), lesson_id, student_id) for lesson_id in lesson_ids]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", vals)

cursor.execute("SELECT value from marks m WHERE m.student_id = %s",
               (student_id,))
print(cursor.fetchall())
cursor.execute("SELECT title FROM books b WHERE b.taken_by_student_id = %s",
               (student_id,))
print(cursor.fetchall())

query = """
SELECT * FROM students s JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = %s
"""

cursor.execute(query, (student_id,))
print(cursor.fetchall())

db.commit()

db.close()
