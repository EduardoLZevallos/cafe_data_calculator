import math
import datetime


def convert_request_to_processors(request):
    """ Each processor can handle 10 request concurrently converts request to processors """
    return math.ceil(request/10)


def convert_processors_to_machines(processors):
    """ Each Machine has 5 processors converts processors to machines """
    return math.ceil(processors / 5)


def apply_additional_capacity(machines, time):
    """ Applies additional capacity of 25% if time is greater than 12:00pm """
    if time >= datetime.time(12, 0):
        additional_capacity = math.ceil(machines * .25)
        machines += additional_capacity
    return machines

