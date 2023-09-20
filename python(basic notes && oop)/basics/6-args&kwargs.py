def f(*args, **kwargs):
    print('args ', args, 'kwargs ', kwargs)

f(1, 2)     # args  (1, 2) kwargs  {}
f(a=10, b=20)   # args  () kwargs  {'a': 10, 'b': 20}
f(1, 2, a=10, b=20) # args  (1, 2) kwargs  {'a': 10, 'b': 20}
# f(a=10, 1)    # SyntaxError: positional argument follows keyword argument

# def f(**kwargs, *args):  # wrong
#     print()


# ==================================================
# if I want to merge two dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}
dic3 = {**dic1, **dic2}
print(dic3)     # {'a': 1, 'b': 2, 'c': 3, 'd': 4}