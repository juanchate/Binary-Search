def binarySearch(orderedArray, numToSearch):
    aux = orderedArray[0]
    while numToSearch != aux:
        halfLen = len(orderedArray)//2
        aux = orderedArray[halfLen]
        if numToSearch > aux:
            orderedArray = orderedArray[halfLen:]
        else:
            orderedArray = orderedArray[:halfLen]
    return aux