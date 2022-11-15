import numpy as np
def calculate_capacity(actual_output):
    result = []
    max_possible_output = 3 * 8670
    for x in actual_output:
        output = (x / max_possible_output) * 100
        result.append(output)
    return result


# def shared_time(power_output):
#     distance = 10
#     index = data['power_output'].argmax()
#     wind_speed = data._get_value(index, "wind_speed")
#     time = distance / wind_speed
#     return time


print(calculate_capacity(list((20))))
