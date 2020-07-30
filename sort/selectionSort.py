def main(): 
    print("~~ SELECTION SORT ~~")
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
    count = selection_sort(el)
    print("# After: ", el)
    print("# N. of operations needed: ", count)

def selection_sort(array):
    count = 0
    for i in range(len(array)):
        count+=1
        ind_min = i
        for j in range(i+1, len(array)):
            count+=1
            if (array[j] < array[ind_min]):
                count=+1
                ind_min = j
        count+=2
        array[i], array[ind_min] = array[ind_min], array[i]
    return count

if (__name__ == "__main__"):
    main()
