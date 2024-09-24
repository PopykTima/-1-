dict1 = {1: 'oma',
         2: 'ama',
         3: {1:'qma', 2:'wma', 3:'rma', 4:'tma', 5:'yma'}, 
         4: 'uma'}
print(dict1)

dict2 = {1: type(dict1[1]),
         2:type(dict1[2]),
         3:type(dict1[3]),
         4:type(dict1[4])}
print(dict2)