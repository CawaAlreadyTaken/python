def main(): 
    print("~~ INSERTION SORT ~~")
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
    count = insertion_sort(el)
    print("# After: ", el)
    print("# N. of operations needed: ", count)

def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        count += 2
        k = array[i]
        j = i-1
        while (j>=0):
            count+=1
            if (k > array[j]):
                break
            count+=2
            array[j+1] = array[j]
            j-=1
        count+=1
        array[j+1] = k
    return count


if (__name__ == "__main__"):
    main()
