def binary_search(l, target):
    left,right = 0,len(l)-1 #where left means the first element of the list which is a index 0
                            #where right means the last element of the list which is a last index i.e (len-1)

    while left <= right:
        mid = (left+right) // 2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1
        
        
if __name__ == "__main__":
    l = [1,3,5,10,12]
    target = 10
    print(binary_search(l,target))
    for i in range(0,9):
        print(i)

