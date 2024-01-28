
from datetime import datetime

abbreviations_file = '../data_files/abbreviations.txt'
start_file = '../data_files/start.log'
end_file = '../data_files/end.log'


def abbreviations_to_dict(text):
    parts = text.strip().split('_')
    key, value = parts[0], f'{parts[1]} | {parts[2]}'
    return {key: value}


def string_to_time(string):
    racer = string[:3]
    stripped_string = string.rstrip()
    time = datetime.strptime(stripped_string[14:], '%H:%M:%S.%f')
    return {racer: time}


def build_report():
    result_abbreviations = []
    with open(abbreviations_file, 'r') as abbreviations:
        for text in abbreviations:
            result_abbreviations.append(abbreviations_to_dict(text))

    result_time_dict = {}
    start_dict = {}
    with open(start_file, 'r') as start:
        for time_start in start:
            start_dict.update(string_to_time(time_start))

    end_dict = {}
    with open(end_file, 'r') as end:
        for time_end in end:
            end_dict.update(string_to_time(time_end))

    for key in set(end_dict.keys()) & set(start_dict.keys()):
        if end_dict[key] > start_dict[key]:
            result_time_dict[key] = end_dict[key] - start_dict[key]
        else:
            result_time_dict[key] = start_dict[key] - end_dict[key]

    sorted_time_result = sorted(result_time_dict.items(), key=lambda item: item[1])
    return result_abbreviations, sorted_time_result


def print_report():
    pass


if __name__ == '__main__':
    build_report()
