
import re

from datetime import datetime
from collections import OrderedDict

abbreviations_file = 'abbreviations.txt'
start_file = 'start.log'
end_file = 'end.log'


def abbreviations_to_dict(text):
    match = re.match(r'(\w+)_(.+)_([^_]+)', text.strip())
    if match:
        key = match.group(1)
        value = f'{match.group(2)} | {match.group(3)}'
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

    return result_abbreviations, result_time_dict


def print_report(path, order='asc', driver=None):
    result_abbreviations, sorted_time_result = build_report(path)
    number = 0
    report_data = []
    if order == 'desc':
        sorted_time_result = OrderedDict(reversed(sorted_time_result.items()))

    if driver == "full":
        return result_abbreviations

    if driver is not None:
        driver = f"{result_abbreviations[driver]} | {sorted_time_result[driver]}"
        report_data.append(driver)
        return report_data

    for key in sorted_time_result:
        number += 1
        result = f"{number}.\t {result_abbreviations[key]} | {sorted_time_result[key]}"
        report_data.append(result)
        if number == 15:
            report_data.append(65 * '*')

    return report_data
