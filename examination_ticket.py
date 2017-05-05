# coding: utf-8

import os
import re

def __get_questions(file_name):
    questions_file = open(file_name, 'r')
    text = questions_file.readlines()
    questions_file.close()

    return text

def __get_question(questions, ticket_number):
    question_index = ticket_number
    while question_index >= len(questions):
        question_index -= len(questions)
    return questions[question_index]

questions_1 = __get_questions('q1.txt')
questions_2 = __get_questions('q2.txt')
questions_3 = __get_questions('q3.txt')

tickets_count = max(len(questions_1), len(questions_2), len(questions_3))
min_tickets_count = 35
if tickets_count < min_tickets_count:
    tickets_count = min_tickets_count

for ticket_number in range(0, tickets_count):
    q1 = __get_question(questions_1, ticket_number)
    q2 = __get_question(questions_2, ticket_number)
    q3 = __get_question(questions_3, ticket_number)

    print ('Билет %s\n1. %s2. %s3. %s' % (str(ticket_number+1), q1, q2, q3))
