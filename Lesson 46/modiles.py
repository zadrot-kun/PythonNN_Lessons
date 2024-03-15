import sys
import os
import pathlib

print('OS')
print('system', os.system('dir'))
for x in os.walk(os.getcwd()):
    print('walk', x)
print('name', os.name)

print('-'*100)
print('SYS')
print('Битность', sys.maxsize / 2**63)
print('platform', sys.platform)

var1 = [1, 2, 3]
# var2 = var1
print('getrefcount', sys.getrefcount(var1))
print('argv', sys.argv)

print('-'*100)

print('pathlib')
path1 = pathlib.Path()
print('cwd', path1.cwd())
print('is_file', path1.is_file())
print('is_dir', path1.is_dir())
path2 = path1 / 'result.txt'
print('path2', path2)
print('resolve', path2.resolve())
print('is_file', path2.is_file())
print('is_dir', path2.is_dir())
for x in path1.iterdir():
    if x.is_file():
        print('  Файл - ', x)
    else:
        print('  Каталог - ', x)

