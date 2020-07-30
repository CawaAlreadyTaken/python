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
    quick_sort_middle(el, 0, n-1)
    print("# After: ", el)

def partition(array, l, h):
    u = (l+h)//2
    array[h], array[u] = array[u], array[h]
    pivot = array[h]
    k = l-1
    for j in range(l, h):
        if (array[j]<=pivot):
            k+=1
            array[k], array[j] = array[j], array[k]
    array[k+1], array[h] = array[h], array[k+1]
    return k+1

def quick_sort_middle(array, l, h):
    if (l<h):
        pivot_index=partition(array, l, h)
        quick_sort_middle(array, l, pivot_index-1)
        quick_sort_middle(array, pivot_index+1, h)
    return  

if (__name__ == "__main__"):
    main()
