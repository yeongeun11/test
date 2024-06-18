# Primitive variables :sol, msg
# Reference variables : bar, foo, kin


bar =[2, 3, 5]

def foo(arg_list):
    cpoied_list = arg_list[:]

    cpoied_list[0] = 100

foo(bar)

print(bar) # 2, 3, 5

def kin(arg_list):
    arg_list[0] = 200

kin(bar.copy())

print(bar)














sol = 4

bar =[3, 4]

foo = [5, 6]

kin = bar

kin[0] = 1

print(bar, foo, kin)

msg = "hello"