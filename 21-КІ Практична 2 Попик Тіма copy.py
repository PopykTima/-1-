a = 'Попик'
b = 'Тіма'
c = 16
list1=[a, b, c]
print(list1)
list2=[type(a), type(b), type(c)]
print(list2)
if type(a) == type(b) == type(c):
    print('Найчастіший тип данних str' )
elif type(a) == type(b) != type(c):
    print('Найчастіший тип данних str' )
else:
    print('Найчастіший тип данних int')