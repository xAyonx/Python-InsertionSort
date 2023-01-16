# Python to insertion Sort 

#Function to Insertion 
def insort(arr):
    if (n := len(arr)) <=1:
        return
    for i in range(1,n):
        key = arr[i]

        #Moving elements in array[0...i-1]
        #that bigger then the key- to one position forward of actuall position

        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] =  key 

        #array elements of [] 
        arr = [8,2,6,4,5]
        insort(arr)
        print(arr)