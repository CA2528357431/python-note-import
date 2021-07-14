# 模块内容私有化


# 在不想被导入的变量、函数、类之前加一个  _
# 即可阻止其被from back import * 结构导入
# 但要用 from back import _name ,
# 或者 import back 后back._name
# 还是可以调用
# 不过当你看到 _ 的时候，别去引用他
from back import *
try:
    print(_name)
except Exception as x:
    print('cannot call _name')
    print(x)
else:
    print('call _name')

print('_'*50)

try:
    print(name)
except Exception as x:
    print('cannot call name')
    print(x)
else:
    print('call name')

