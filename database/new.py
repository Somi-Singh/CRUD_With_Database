# def occurenc():
#     i=0
#     empty=[]
#     while i<len(my_list):
#         j=0
#         empty2=[]
#         count=0
#         while j<len(my_list):
#             if my_list[i]==my_list[j]:
#                 count=count+1
#             j=j+1
#         empty2.append(my_list[i])
#         empty2.append(count)
#         if empty2 not in empty:
#             empty.append(empty2)
#         i=i+1
#     print(empty)
# my_list=[10,10,10,10,20,20,20,20,40,40,50,50,30]
# occurenc()


def frequency(list1):
    i=0
    empty={}
    while i<len(list1):
        j=0
        count=0
        while j<len(list1):
            if list1[i]==list1[j]:
                count=count+1
            j=j+1
        empty[list1[i]]=count
        i=i+1
    print(empty)
list1=[1,1,1,2,2,3,4,4,5]
frequency(list1)