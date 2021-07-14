# package

#所谓packa实际上是一个特殊的文件夹，其内部必须要有 __init__.py 这一文件
#import时可直接引入包中全部模块

#注意在__init__中将包中模块引入，具体见文件操作

import package1
a=package1.send.send(109)
b=package1.do.do(a)
c=package1.receive.receive(b)
print(c)
