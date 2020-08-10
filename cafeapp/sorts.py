def mergeSort(arr): 
    
    """ Runtime """ 
    # Best Case: O(n log n)
    # Worst Case: O(n log n)

    if len(arr) <= 1: 
        return arr
    
    left_list = mergeSort(arr[0:len(arr)//2])
    right_list = mergeSort(arr[len(arr)//2: len(arr)])

    return merge(left_list, right_list)

def merge(list1, list2):

    """ Runtime """ 
    # O(n + m)

    sortedlist = [] 

    while list1 and list2: 
        if list1[0] < list2[0]: 
            sortedlist.append(list1[0])
            list1 = list1[1:]
        else: 
            sortedlist.append(list2[0])
            list2 = list2[1:]
    
    if list1: 
        sortedlist += list1

    if list2: 
        sortedlist += list2

    return sortedlist