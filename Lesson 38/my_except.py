
import module_middle
from module import MyException


try:
    module_middle.func2()
except Exception as exp:
    print(exp)
    print(exp.args)
    print('выполнено с ошибкой')
else:
    print('выполнено без ошибки')