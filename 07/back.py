def fun1(*args,**kwargs):

    print('args  ',args)
    print('kwargs',kwargs)


def fun2(*args,**kwargs):
    fun1(args,kwargs)


def fun3(*args,**kwargs):
    fun1(*args,**kwargs)