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
    count = quick_sort_low(el, 0, n-1, 0)
    print("# After: ", el)
    print("# N. of operations needed: ", count)

def partition(array, l, h, count):
    count+=2
    k = l
    pivot = array[l]
    for j in range(l+1, h+1):
        count+=1
        if (array[j]<=pivot):
            count+=3
            k+=1
            array[k], array[j] = array[j], array[k]
    count+=2
    array[k], array[l] = array[l], array[k]
    return count, k

def quick_sort_low(array, l, h, count):
    count+=1
    if (l<h):
        count+=3
        a, pivot_index=partition(array, l, h, count)
        count+=a
        quick_sort_low(array, l, pivot_index-1, count)
        quick_sort_low(array, pivot_index+1, h, count)
    return count 

if (__name__ == "__main__"):
    main()
