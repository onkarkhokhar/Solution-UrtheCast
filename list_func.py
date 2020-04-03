from collections import Counter
li=list(input().split())
add_list=list(input().split())
del_list=list(input().split())
for item in add_list:
    li.append(item)
for item in del_list:
    if item in li:
        li.remove(item)
    else:
        print("Item not present in list")

new_li=Counter(li)
for i in new_li.most_common():
    print(i)
