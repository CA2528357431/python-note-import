# 拆包引入
import back

print('fun1')
back.fun1(1,2,3,4,a=1,b=2)

print()

print('fun2')
back.fun2(1,2,3,4,a=1,b=2)
# args在函数中视为元组，kwargs被视为dic
# 二者在fun2中被带入了args

print()

print('fun3')
back.fun3(1,2,3,4,a=1,b=2)
# 如果带入时写作*args与**kwargs，
# 则将他们拆开，视作大量独立对象和等式