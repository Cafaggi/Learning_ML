''' Lambda functions accepts arguments on the left side and use them on the rigth side. 
    Lambda functions are only another type of function objects'''


def func_(a: int):
    print('runung func_1')

a= type(func_)
print(a)

fnl = lambda x : x**2
print(type(fnl))


afl = lambda x,y : x*y

print(afl(4,5))