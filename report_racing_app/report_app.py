
from datetime import datetime
from collections import OrderedDict

abbreviations_file = 'abbreviations.txt'
start_file = 'start.log'
end_file = 'end.log'


def abbreviations_to_dict(text):
    parts = text.strip().split('_')
    key, value = parts[0], f'{parts[1]} | {parts[2]}'
    return {key: value}


def string_to_time(string):
    racer = string[:3]
    stripped_string = string.rstrip()
    time = datetime.strptime(stripped_string[14:], '%H:%M:%S.%f')
    return {racer: time}


def build_report(path):
    result_abbreviations = {}
    with open(f'../{path}/{abbreviations_file}', 'r') as abbreviations:
        for text in abbreviations:
            result_abbreviations.update(abbreviations_to_dict(text))

    result_time_dict = {}
    start_dict = {}
    with open(f'../{path}/{start_file}', 'r') as start:
        for time_start in start:
            start_dict.update(string_to_time(time_start))

    end_dict = {}
    with open(f'../{path}/{end_file}', 'r') as end:
        for time_end in end:
            end_dict.update(string_to_time(time_end))

    for key in set(end_dict.keys()) & set(start_dict.keys()):
        if end_dict[key] > start_dict[key]:
            result_time_dict[key] = end_dict[key] - start_dict[key]
        else:
            result_time_dict[key] = start_dict[key] - end_dict[key]

    sorted_time_result = OrderedDict(sorted(result_time_dict.items(), key=lambda item: item[1]))
    return result_abbreviations, sorted_time_result


def print_report(path, sort='asc', driver=None):
    result_abbreviations, sorted_time_result = build_report(path)
    number = 0

    if sort == 'desc':
        sorted_time_result = OrderedDict(reversed(sorted_time_result.items()))

    if driver is not None:
        return print(f"{result_abbreviations[driver]} | {sorted_time_result[driver]}")

    for key in sorted_time_result:
        number += 1
        print(f"{number}.\t {result_abbreviations[key]} | {sorted_time_result[key]}")
        if number == 15:
            print(70 * '*')
