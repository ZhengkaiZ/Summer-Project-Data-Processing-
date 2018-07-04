from sets import Set

def remove_static_list_all_day(device_list):
    result = Set()
    for key in device_list.keys():
        if (device_list[key] > 4300):
            result.add(key)
    return result
