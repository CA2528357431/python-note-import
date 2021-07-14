# 调用本文建之外的模块

# 模块位于 E:\PYTHON BASE\import\03TEST

import sys

for x in sys.path:
    print(x)
# 可见path中把并没有模块所在的路径，添加上即可
print()
sys.path.append(r'E:\PYTHON BASE\import\03TEST')


import back

print(back.dog)
