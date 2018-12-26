num_int = [1,2,3,8,9,21,23,333,3333,33]
i = 0
summary=0

while i < len(num_int):
    summary += num_int[i]
    i+=1
print(summary)
for i in range(len(num_int)):
    summary += num_int[i]
print(summary)


def list_summary(some_list):
    if len(some_list) > 1:
        some_list[0] += some_list.pop(1)
        return list_summary(some_list)
    else:
        return some_list[0]

print(list_summary(num_int))
def list_summary(some_list,summary):
    if len(some_list) > 0:
        summary += some_list.pop(0)
        return list_summary(some_list,summary)
    else:
        return summary
summary = 0
print(list_summary(num_int,summary))