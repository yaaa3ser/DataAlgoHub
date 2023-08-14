def f(a,/):
    print(a)

# f(a=1) # f() got some positional-only arguments passed as keyword arguments: 'a'

def f2(a, *, b):
    print(a, b)
    
# f2(1, 2) # f2() takes 1 positional argument but 2 were given




