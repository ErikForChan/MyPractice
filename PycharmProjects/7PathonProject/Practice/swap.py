# 冒泡排序
arr = [2,6,8,1,9,56,77]


def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


# newArr = bubblesort(arr)
#
# for data in newArr:
#     print("data: "+str(data))

# 插入排序

def insertsort(arr):
    for i in range(len(arr)): # arr = [1,2,8,8,9,56,77]
        preIndex = i - 1 #0 1 2 1
        curData = arr[i] #6 8 1 最小的那个数，要放到第一位
        while preIndex >= 0 and arr[preIndex] > curData: # 如果前面一个数大于后面一个数
            arr[preIndex+1] = arr[preIndex] # 讲相邻连个数换位
            preIndex -= 1
        arr[preIndex + 1] = curData
        # for j in range(i+1,len(arr)):
        #     if arr[i] > arr[j]:
        #         arr[i],arr[j] = arr[j],arr[i]
    return arr


newArr = insertsort(arr)

for data in newArr:
    print("data1: "+str(data))