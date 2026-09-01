class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_id, origin_city, dest_id, dest_city, out_date, return_date, flight_stops):
        self.price = price
        self.origin_iata_code = origin_id
        self.origin_city = origin_city
        self.dest_iata_code = dest_id
        self.dest_city = dest_city
        self.out_date = out_date
        self.return_date = return_date
        self.stops = flight_stops


def make_flight_list(data, out_date, return_date):
    list_of_flights = []
    origin_id = data["airports"][0]["departure"][0]['airport']['id']
    origin_city = data["airports"][0]["departure"][0]["city"]
    dest_id = data["airports"][0]["arrival"][0]['airport']['id']
    stops = str(int(data["search_parameters"]["stops"]) - 1)
    dest_city = data["airports"][0]["arrival"][0]["city"]
    for key in data["best_flights"]:
        price = key["price"]
        flight_found = FlightData(price, origin_id, origin_city, dest_id, dest_city, out_date, return_date, stops)
        list_of_flights.append(flight_found)
    for key in data["other_flights"]:
        price = key["price"]
        flight_found = FlightData(price, origin_id, origin_city, dest_id, dest_city, out_date, return_date, stops)
        list_of_flights.append(flight_found)

    return list_of_flights

def find_cheapest_flight(data, out_date, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
         print("No flight data")
         return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    flight_list = make_flight_list(data, out_date, return_date)
    cheap_flight = None
    for flight in flight_list:
        try:
            if flight.price < cheap_flight.price:
                cheap_flight = flight
        except AttributeError:
            cheap_flight = flight
    return cheap_flight
