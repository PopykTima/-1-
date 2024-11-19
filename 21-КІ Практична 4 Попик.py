anaconda_list = [3,1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']
right_list = []

def anaconda(anaconda_list):
    for chislo in anaconda_list:
        if chislo not in right_list:
            right_list.append(chislo)
    return right_list

def sort_anaconda(anaconda):
    num_list = []
    str_list = []
    for i in anaconda:
        if type(i) == int:
            num_list.append(i)
        elif type(i) == str:
            str_list.append(i)
    num_list.sort()
    str_list.sort(key=str.lower)
    return num_list + str_list

result_anaconda = anaconda(anaconda_list)
sorted_anaconda = sort_anaconda(result_anaconda)


        
print(anaconda(anaconda_list))
print(sort_anaconda(result_anaconda))