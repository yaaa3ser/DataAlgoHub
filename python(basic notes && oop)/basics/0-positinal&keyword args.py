def f(a,/): # / means everything before it is positional-only args
    return a
    
    
print(f(1)) # ok because 1 is positional arg

print(f(a=1))
# TypeError: f() got some positional-only arguments passed as keyword arguments: 'a'

# ============================================================

def f2(a, *, b): # * means everything after it is keyword-only args
    print(a, b)
    
f2(1, b=2) # ok
f2(1, 2) 
# f2() takes 1 positional argument but 2 were given




