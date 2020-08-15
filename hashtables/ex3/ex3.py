def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #storage dict
    storage ={}
    #loop through main array
    for i in arrays:
         #loop through array
        for j in i:
            #if entry not in dict
            if j not in storage:
                #add to dict with value of 1
                storage[j] = 1
            else:
                #increment value at key
                storage[j] += 1
    
    #loop through keys and grab all keys with values greater than 1
    result = [k for k,v in storage.items() if v > 1]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
