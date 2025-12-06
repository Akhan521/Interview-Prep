'''
Problem 5: Find Itinerary
You are a traveler about to embark on a multi-leg journey with multiple flights to arrive at your final travel destination. You have all your 
boarding passes, but their order has gotten all messed up! You want to organize your boarding passes in the order you will use them, from your 
first flight all the way to your last flight that will bring you to your final destination.

Given a list of edges boarding_passes where each element boarding_passes[i] = (departure_airport, arrival_airport) represents a flight from 
departure_airport to arrival_airport, return an array with the itinerary listing out the airports you will pass through in the order you will 
visit them. Assume that departure is scheduled from every airport except the final destination, and each airport is visited only once (i.e., 
there are no cycles in the route).

def find_itinerary(boarding_passes):
    pass
    
Example Usage:
boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))

Example Output:
['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
'''

def find_itinerary(boarding_passes):
    '''
    Plan:
    1. Create a mapping of departure airports to arrival airports using a dictionary.
    2. Identify the starting airport by finding the airport that is a departure point but not an arrival point.
    3. Initialize the itinerary list and start from the identified starting airport.
    4. Use a loop to traverse through the boarding passes, appending each airport to the itinerary until there are no more flights.
    5. Return the completed itinerary list.
    '''
    # Step 1: Create a mapping of departure to arrival airports
    flight_map = {}
    all_arrivals = set()

    for departure, arrival in boarding_passes:
        flight_map[departure] = arrival
        all_arrivals.add(arrival)

    # Step 2: Identify the starting airport
    start = None
    for departure in flight_map:
        if departure not in all_arrivals:
            start = departure
            break

    # Step 3: Trace the itinerary
    itinerary = []
    current = start
    while current:
        itinerary.append(current)
        current = flight_map.get(current)

    return itinerary

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))