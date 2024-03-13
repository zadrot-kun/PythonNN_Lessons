import re

source_str = 'Добрый день, колллеги!'
re_str = 'день'


match1 = re.search(re_str, source_str)
print(match1.start(), match1.end())

print('-'*100)

re_str2 = 'Добрый день'
match2 = re.match(re_str2, source_str)
print(match2.start(), match2.end())

print('-'*100)

re_str3 = 'Добрый день, колллеги!'
match3 = re.fullmatch(re_str3, source_str)
print(match3.start(), match3.end())

print('-'*100)

re_str4 = 'о'
print(re.split(re_str4, source_str))

print('-'*100)

re_str5 = '(о)([\w])+'
print(re.findall(re_str5, source_str))

print('-'*100)

re_str5 = '(о)([\w])+'
for x in re.finditer(re_str5, source_str):
    print(x)

print('-'*100)

re_str6 = '(день)([,]+)'
sub_str = r'\2\1'
print(re.sub(re_str6, sub_str, source_str))

print('-'*100)

source_str2 = 'asddsertrt'
re_str7 = r'([\w]+)\1'
print(re.findall(re_str7, source_str2))

print('-'*100)

print(re.subn(re_str6, sub_str, source_str))

print('-'*100)

re_str8 = re.compile(r'([\w]+)\1')
print(re.findall(re_str8, source_str2))
