INSERT INTO students (name, second_name, group_id) VALUES ('Gena', 'Bukin2', 25001)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Schastlivy vmeste 2', 'Apr 2005', 'May 2010')

INSERT INTO books (title, taken_by_student_id) VALUES ('3 Porosenka', 23230)

INSERT INTO books (title, taken_by_student_id) VALUES ('4 Porosenka', 23230)

INSERT INTO subjects (title) VALUES ('Sopromat')

INSERT INTO subjects (title) VALUES ('Termex')

INSERT INTO lessons (title, subject_id) VALUES ('Vstuplenie', 23468)

INSERT INTO lessons (title, subject_id) VALUES ('Glava 1', 23468)

INSERT INTO lessons (title, subject_id) VALUES ('Vvedenie', 23469)

INSERT INTO lessons (title, subject_id) VALUES ('Chast 1', 23469)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('99', 76984, 23230)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('90', 76985, 23230)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('76', 76986, 23230)

INSERT INTO marks (value, lesson_id, student_id) VALUES ('85', 76987, 23230)

SELECT value from marks m WHERE m.student_id = 23230

SELECT title FROM books b WHERE b.taken_by_student_id = 23230

SELECT * FROM students s JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = 23230