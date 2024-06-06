# Identity operator
# is, is not

bar = [2, 3, 4]
foo = [2, 3, 4]
pos = bar

if bar == foo:
    print("참")
else:
    print("거짓")    

if bar is foo:
    print("참")
else:
    print("거짓")

if bar is pos:
    print("참")
else:
    print("거짓")            