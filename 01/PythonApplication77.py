# import

import cat_module  # 导入

a = cat_module.cat()
print("cat")
a.run()
print(cat_module.health, " ", cat_module.speed)
print(cat_module.cat.cute)
print(a.live)

print()

import dog_module as dog  # 简化模块名字

b = dog.dog()
print("dog")
b.run()
print(dog.health, " ", dog.speed)
print(dog.dog.cute)
print(b.live)

print()

from elephant_module import hool  # 引入部分功能

hool()  # 此函数不加模块名直接用

from dog_module import special
from elephant_module import special
from cat_module import special

print(special)
# 若名字一样则后引入的覆盖新引入的


# “模块中直接执行的部分” 不需要 在main文件中被执行
# 本例中各模块的“test”就是这样

# 修改于模块“test”处

# 本文件中 __name__ 是 main
# 引入模块中 __name__ 是模块名
