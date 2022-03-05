from sympy import *

def sympy_derivative():
    # 定义表达式的变量名称
    x = symbols('x')
    # 定义表达式内容
    y = x*x*x + x
    # 计算 x2对应的偏导数
    return diff(y, x)

func = sympy_derivative()
print(func) # 输出结果2*x26
print(func.evalf(subs ={'x':6})) # 把x2 等于 带入计算 结果 为12