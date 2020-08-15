def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    #storage dict
    storage ={}
    #loop through a
    for i in a:
        new_num = i
        if i < 0:
            new_num = i * -1 
        #if abs of entry is not in dict
        if new_num not in storage: 
            # add it as key with 1 as value
            storage[new_num] = 1
        else:
            #increment value at abs of entry
            storage[new_num] += 1

    result = [k for k,v in storage.items() if v > 1]
    
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
