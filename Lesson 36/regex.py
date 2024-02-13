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
print('-'*100)
source_text = '30.12.1924'
print(re.findall(r'[0-3][0-9]\.[01][0-9]\.[12][90][0-9][0-9]', source_text))
print('-'*100)
source_text = '''
def finc1():
    """Моя первая
    программа"""
    print("""Hello world""")
'''
print(re.findall(r'def [^\(]+\([^\)]*\):\s+"""([^"]+)"""', source_text))
print('-'*100)
source_text = '''
  <head></head>
  <body>
    <h1>Заголовок</h1>
    <div>
    Рад Вас приветствовать <div>Друзья</div>
    </div>
  </body>
'''
print(re.findall(r'(<(\w+)>[^\2]*</\2>)', source_text))
print('-'*100)
source_text = '''
    Вложение для презентации Чуланову
'''
print(re.sub(r'(Чуланов\w+)','\1 Г.С.', source_text))