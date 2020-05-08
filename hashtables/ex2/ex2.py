#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    trip = {}

    for ticket in tickets:
        trip[ticket.source] = ticket.destination
    
    # [print(i, trip[i]) for i in trip]
    # print()
    tracker = 'NONE'
    route = [trip[tracker]]
    tracker = trip[tracker]
    while tracker != 'NONE':
        route.append(trip[tracker])
        tracker = trip[tracker]

    return route
