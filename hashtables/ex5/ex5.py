# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #result array
    result = []
    #storage dict
    storage = {}
    #loop through files
    for i in files:
        #split the file on '/'
        farr = i.split('/')
        key = farr[len(farr) - 1] 
        #grab the last index
        #if last index is not in storrage
        if key not in storage:
            #set last index to key and file into array value
            storage[key] = [i]
        else:
            #append filenalme to last index key
            storage[key].append(i) 

    #loop through querries
    for i in queries:
        #if querry in storage dict
        if i in storage:
            #add value arry to result arry
            result += storage[i]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
