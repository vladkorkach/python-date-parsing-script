#!/usr/bin/python3
import argparse
import datetime
import collections


def get_arguments():
    """
    Add arguments to python script
    """
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file")

    return argparser.parse_args()


def format_num_as_date(num: str) -> int:
    """
    Changes input date data from str to int.

    :param num: A string. Year, month or day.
    :return: An integer. Year, month or day.
    """

    number = int(num)

    if number is 0:
        return 2000

    return number


def get_data(file):
    """
    Read input data from file

    :param file: file (prefer text file)
    :return: A string. Initial data from the file
    """

    with open(file) as f:
        initial_data = f.readline()

    return initial_data


def parse_num(initial_data: str) -> list:
    """
    :param initial_data: A string. Initial date data.
    :return: A list. The date data splitted in list by '/'.
    """

    numbers = initial_data.split('/')

    return list(sorted(map(format_num_as_date, numbers)))


def is_date_valid(input_date: str) -> bool:
    """
    Check if year is valid

    :param input_date: formatted date by '-'
    :return: A bool
    """

    date = datetime.datetime.strptime(input_date, '%Y-%m-%d')

    if date.year < 2000 or date.year > 2999:
        raise ValueError()

    return True


def date_generator(numbers: list) -> str:
    """
    Function generates date in valid format. It checks if year, month or day is invalid and
    does necessary changes in date list. If year is invalid (< 2000 or > 2999) so it raises
    ValueError by function `is_date_valid`.

    :param numbers: A list. The numbers from input date data that splitted by '/' in list.
    :return: A string. Valid date.
    """

    date_indices = collections.deque([0, 1, 2])

    for x in range(0, 2):
        m = numbers[date_indices[1]]
        d = numbers[date_indices[2]]

        if d > 31 or m > 12:
            date_indices.rotate(1)

    y = numbers[date_indices[0]]
    m = numbers[date_indices[1]]
    d = numbers[date_indices[2]]

    if y < 2000:
        y += 2000

    date = '{y}-{m:02d}-{d:02d}'.format(y=y, m=m, d=d)

    # It raises ValueError if year isn't valid.
    is_date_valid(date)

    return date


def main():
    arguments = get_arguments()
    input_data = get_data(arguments.file)
    numbers = parse_num(input_data)

    try:
        date = date_generator(numbers)
        print(date)
    except ValueError:
        print('is illegal')


if __name__ == "__main__":
    main()
