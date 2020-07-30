def main(): 
    print("~~ QUICK SORT, PIVOT: LOW ~~")
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
    quick_sort_low(el, 0, n-1)
    print("# After: ", el)

def partition(array, l, h):
    k = l
    pivot = array[l]
    for j in range(l+1, h+1):
        if (array[j]<=pivot):
            k+=1
            array[k], array[j] = array[j], array[k]
    array[k], array[l] = array[l], array[k]
    return k

def quick_sort_low(array, l, h):
    if (l<h):
        pivot_index=partition(array, l, h)
        quick_sort_low(array, l, pivot_index-1)
        quick_sort_low(array, pivot_index+1, h)
    return 

if (__name__ == "__main__"):
    main()
