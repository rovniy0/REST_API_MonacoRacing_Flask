
import datetime

abbreviations_file = '../data-files/abbreviations.txt'
start_file = '../data-files/start.log'
eng_file = '../data-files/end.log'


def abbreviations_to_dict(text):
    parts = text.strip().split('_')
    key, value = parts[0], f'{parts[1]} | {parts[2]}'
    return {key: value}


def build_report():
    with open(abbreviations_file, 'r') as abbreviations:
        for text in abbreviations:
            result_abbreviations = abbreviations_to_dict(text)


def print_report():
    pass


if __name__ == '__main__':
    build_report()
