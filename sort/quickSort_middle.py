def main(): 
    print("~~ QUICK SORT, PIVOT: MIDDLE ~~")
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
    count = quick_sort_middle(el, 0, n-1, 0)
    print("# After: ", el)
    print("# N. of operations needed: ", count)

def partition(array, l, h, count):
    count+=2
    u = (l+h)//2
    array[h], array[u] = array[u], array[h]
    pivot = array[h]
    k = l-1
    for j in range(l, h):
        count+=1
        if (array[j]<=pivot):
            count+=3
            k+=1
            array[k], array[j] = array[j], array[k]
    count+=2
    array[k+1], array[h] = array[h], array[k+1]
    return count, k+1

def quick_sort_middle(array, l, h, count):
    count+=1
    if (l<h):
        count+=3
        a, pivot_index=partition(array, l, h, count)
        count+=a
        quick_sort_middle(array, l, pivot_index-1, count)
        quick_sort_middle(array, pivot_index+1, h, count)
    return count 

if (__name__ == "__main__"):
    main()
