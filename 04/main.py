# 对模块进行reload


import back

print()
print('start')

back.do()
print('mid')

import back

back.do()

print('end')
print('-' * 50)

# 当程序没有执行结束，默认情况下外界对文件的改变不会影响执行
# 中间再加import也没用，因为会被识别为重复导入，第二个import直接失效




from importlib import reload

print()
print('start')

back.do()
print('mid')


reload(back)
back.do()

print('end')

# 使用reload可以对模块重新加载
# 使用逐步调试进行验证
# 修改完模块记得保存

