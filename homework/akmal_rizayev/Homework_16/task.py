import os
import csv
from csv import DictReader

import mysql.connector as mysql
from dotenv import load_dotenv

dotenv = load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)

cursor = db.cursor(dictionary=True)

base_table = '''
SELECT s.name, s.second_name, g.title AS group_title,
 b.title AS book_title, sb.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
FROM students AS s
JOIN `groups` AS g ON s.group_id = g.id
JOIN books AS b ON b.taken_by_student_id = s.id
JOIN marks AS m ON m.student_id = s.id
JOIN lessons AS l ON l.id = m.lesson_id
JOIN subjects AS sb ON sb.id = l.subject_id
'''

file_path = os.path.join('..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path) as csvfile:
    file_data = csv.DictReader(csvfile)
    for row in file_data:
        cursor.execute(f'''
        SELECT * FROM ({base_table}) AS base_table WHERE name = %s AND second_name = %s
        AND group_title = %s AND book_title = %s AND subject_title = %s
        AND lesson_title = %s AND mark_value = %s
        ''', (row['name'], row['second_name'],
              row['group_title'], row['book_title'], row['subject_title'],
              row['lesson_title'], row['mark_value']))
        if not cursor.fetchall():
            print(row)
