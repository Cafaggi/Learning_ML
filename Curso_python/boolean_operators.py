'''
When an object is truthy in an 'or' operator is returned itself.  None type has a falsy value
'''

lista1 = [1,3,4]
lista2 = list()
lista3 = None


a=  lista2 if lista2 else lista1
print(a)

a = lista1 or lista2 or lista3
print(a)

a = lista3 and lista2 or lista1
print(a)

