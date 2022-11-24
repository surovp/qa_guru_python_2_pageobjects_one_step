from typing import Tuple


#Функция для склейки предметов из кортежа для проверки
def subjects_line_formatter(subjects: Tuple):
    line = ''
    for subject in subjects:
        line = line + str(subject) + ', '
    line = line.rstrip(', ')
    return line
