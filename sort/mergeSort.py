def main(): 
    print("~~ MERGE SORT ~~")
    print("# I need: the number of elements and the elements.")
    n = int(input("# Number of elements: "))
    print("# Elements:\n")
    el = []
    i = 0
    while(i<n):
        flag = False
        a = input("- ")
        for c in a:
            if (c<'0' or c>'9'):
                print("# You need to insert a number.")
                flag = True
                break
        if not flag:
            i+=1
            el.append(int(a))
    print("# Before: ", el)
    merge_sort(el)
    print("# After: ", el)

def merge_sort(array):
    half = len(array)//2
    left = array[:half]
    right = array[half:]
    if (len(array)>1):
        merge_sort(left)
        merge_sort(right)
    i = 0
    j = 0
    array1 = []
    while(i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            array1.append(left[i])
            i+=1
        else:
            array1.append(right[j])
            j+=1
    while(i<len(left)):
        array1.append(left[i])
        i+=1
    while(j<len(right)):
        array1.append(right[j])
        j+=1
    for i in range(len(array1)):
        array[i] = array1[i]
    return


if (__name__ == "__main__"):
    main()
