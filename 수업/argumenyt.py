# argument

# 1) positional argment 
def foo(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)

foo(1, 2, 3)

# 2) keyword areument

def pos(arg_a, arg_b, arg_c):
    print(arg_a, arg_b, arg_c)

pos(arg_a = 1, arg_b = 2, arg_c = 3)

# 3) default argument
def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4):
    print(arg_a, arg_b, arg_c, arg_d)

kin()
kin(6, 7, 8, 9)
kin(6)
kin(6, 7)
kin(6, 7, arg_d=10)

print("hello", end = "")


