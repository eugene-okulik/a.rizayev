import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Gena', 'Bukin4')")
student_id = cursor.lastrowid
cursor.execute("INSERT INTO `groups` (title, start_date, end_date)"
               " VALUES ('Schastlivy vmeste 4', 'Apr 2005', 'May 2010')")
group_id = cursor.lastrowid
query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query, (group_id, student_id))

cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('1 Porosenok', %s)", (student_id,))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('2 Porosenka', %s)", (student_id,))

cursor.execute("INSERT INTO subjects (title) VALUES ('Novaya Matematika')")
subj1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES ('Novaya Fizika')")
subj2_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Lesson 1', %s)",
               (subj1_id,))
lesson_1 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Lesson 2', %s)",
               (subj1_id,))
lesson_2 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Lesson first', %s)",
               (subj2_id,))
lesson_3 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Lesson second', %s)",
               (subj2_id,))
lesson_4 = cursor.lastrowid

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('65', %s, %s)",
               (lesson_1, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('66', %s, %s)",
               (lesson_2, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('67', %s, %s)",
               (lesson_3, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES ('68', %s, %s)",
               (lesson_4, student_id))

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
