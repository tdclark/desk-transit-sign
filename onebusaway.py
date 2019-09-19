import requests
import collections

ArrivalAndDeparture = collections.namedtuple("ArrivalAndDeparture",
                                             "route_name_long, route_name_short, scheduled_arrival_time")


class OneBusAwayClient:
    API_ENDPOINT = "http://api.pugetsound.onebusaway.org/api/where"
    METHOD_ARR_AND_DEP_FOR_STOP = "arrivals-and-departures-for-stop"

    def __init__(self, default_agency_id, api_key):
        self.default_agency_id = default_agency_id
        self.api_key = api_key

    def __build_stop_id(self, stop_id, agency_id=None):
        if agency_id is None:
            agency_id = self.default_agency_id

        return "{}_{}".format(agency_id, stop_id)

    def get_arrivals_and_departures_for_stop(self, stop_id):
        formatted_stop_id = self.__build_stop_id(stop_id)
        api_url = "{}/{}/{}.json".format(OneBusAwayClient.API_ENDPOINT,
                                         OneBusAwayClient.METHOD_ARR_AND_DEP_FOR_STOP,
                                         formatted_stop_id)

        response = requests.get(api_url, {'key': self.api_key})
        response_json = response.json()

        arrivals_and_departures = list()
        for entry in response_json["data"]["entry"]["arrivalsAndDepartures"]:
            route_name_long = entry["routeLongName"]
            if route_name_long == "":
                route_name_long = None
            route_name_short = entry["routeShortName"]
            scheduled_arrival_time = entry["scheduledArrivalTime"]
            arrival_and_departure = ArrivalAndDeparture(route_name_long=route_name_long,
                                                        route_name_short=route_name_short,
                                                        scheduled_arrival_time=scheduled_arrival_time)
            arrivals_and_departures.append(arrival_and_departure)

        return arrivals_and_departures
