dict1 = {1: 'oma',
         2: 'ama',
         3: {1:'qma', 2:'wma', 3:'rma', 4:'tma', 5:'yma'}, 
         4: 'uma'}
print(dict1)

type_dict ={}
for key in dict1:
    box = dict1[key]
    if type(box) == dict:
        for my_key in box:
            my_box = type(box[my_key])
            type_dict[my_key] = type[my_box]
        else:
            type_dict[key] = type(box)
print(type_dict)    
