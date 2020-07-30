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
    selection_sort(el)
    print("# After: ", el)

def selection_sort(array):
    for i in range(len(array)):
        ind_min = i
        for j in range(i+1, len(array)):
            if (array[j] < array[ind_min]):
                ind_min = j
        array[i], array[ind_min] = array[ind_min], array[i]
    return 

if (__name__ == "__main__"):
    main()
