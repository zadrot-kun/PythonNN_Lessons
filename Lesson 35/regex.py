# Проверить, что текст письма содержит приветствие Добрый день!
# Проверить, что текст письма содержит приветствие Добрый день! (восклицательный знак опционален)
# Проверить, что текст письма содержит приветствие Добрый день! или Привет!
# Найти google с любым кол-вом o
# Найти google с любым кол-вом oog
# текст начинается с большой буквы, а заканчивается точкой
# Валидация формата даты
# Проверить, что каждая функция содержит комментарий
# Найти все html теги
# Заменить Чуланов на ФИО (окончания фамилии в группу)

import re

source_text = """ 
Ян, Привет!
Просьба отвеить на моё письмо ниже."""

print(re.findall('^\\s*[а-яА-Я]{2,}, ([дД]обрый день[\\.!]|Привет!)', source_text))
print('-'*100)
print(re.findall('g(?:oog)+le', 'googoogoogoogoogoogle'))
print('-'*100)
source_text = """Ян, Привет!
Просьба отвеить на моё письмо ниже."""
print(re.findall('(?s)^[А-Я].*\\.$', source_text))