my_list = [1,[2, [3], [1, 2]], 4]
j=0
i = 0
p=0
sum = 0
while i < len(my_list):
    if type(my_list[i]) == int:
       sum +=  my_list[i]
    elif type(my_list[i]) == list:
        while j < len(my_list[i]):
            if type(my_list[i][j]) == int:
                sum += my_list[i][j]
            elif type(my_list[i][j] == list):
                p = 0
                while p < len(my_list[i][j]):
                    sum += my_list[i][j][p]
                    p+=1
            j += 1
    i+= 1
print (sum)'''
'''sum = 0
my_list = [1, [2, [3], [1, 2]], 4]
for i in range(len(my_list)):
    if type(my_list[i]) == int:
        sum += my_list[i]
    elif type(my_list[i]) == list:
        for j in range(len(my_list[i])):
            if type(my_list[i][j]) == int:
                sum += my_list[i][j]
            elif type(my_list[i][j] == list):
                for p in range(len(my_list[i][j])):
                    sum += my_list[i][j][p]
print (sum)

def list_sum (some_list):
    sum = 0
    for i in range (len(some_list)):
        if type(some_list[i]) == int:
            sum += some_list[i]
        elif type(some_list[i]) == list:
            sum += list_sum(some_list[i])
    return sum

my_list = [1,[2, [3], [1, 2]], 4]
print (list_sum(my_list))
def list_sum(some_list):
    for i in range(len(some_list)):
        if type(some_list[i]) == int:
            if some_list[i] == some_list[0]:
                pass
            else:
                some_list[0] += some_list[i]
        elif type(some_list[i]) == list:
            some_list[0] += list_sum(some_list[i])

    return  some_list[0]

my_list = [1,[2, [3], [1, 2]], 4]
print (list_sum(my_list))