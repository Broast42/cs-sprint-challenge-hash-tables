#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    storage = {}
    #loop through tickets
    for i in tickets: 
        #add each tickets source to a dict as a key and destination as value
        storage[i.source] = i.destination
    
    #var dict[None]
    current = storage['NONE']
    index = 0
    # while var is not none:
    while index != length:
        #append value to route
        route.append(current)
        #var = dict[var]
        current = storage[current]
        index += 1

    return route
