# from import *与import 的本质差别

import hk1

print(hk1.xxx)
hk1.xxx = False
hk1.check()


print('-' * 50)


from hk2 import *

print(xxx)
xxx = False
check()

# from import * 是在本文件中重新创建模块中的同名对象
# import 则是直接对模块中原有的对象进行操作
