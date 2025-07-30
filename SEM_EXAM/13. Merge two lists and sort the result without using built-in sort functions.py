list1 = [5, 1, 9]
list2 = [3, 7, 2]
merged_list = list1 + list2
n=len(merged_list)
for i in range (0,n):
    for j in range (i,n):
        if merged_list[i]>merged_list[j]:
            temp=merged_list[i]
            merged_list[i]=merged_list[j]
            merged_list[j]=temp
print("Merged and sorted list: ",merged_list)