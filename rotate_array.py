
def rightrotate():
    arr = [1,2,3,4,5,6]
    n=4
    sarr = []
    sarr = arr[len(arr)-n:len(arr)]
    sarr+=arr[:len(arr)-n]

            
    print(sarr)

def leftrotate():
    arr = [1,2,3,4,5,6]
    n=2
    sarr = []
    sarr = arr[n:len(arr)]
    sarr+=arr[0:n]

            
    print(sarr)

    
rightrotate()

leftrotate()

