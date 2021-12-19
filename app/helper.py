from math import ceil, pow
from os import linesep
import re

from app.validator import isFileSize



def prepare_filter_config(argv):
    conditions = {
        "minimum_size": 0,
        "maximum_size": float("inf"),
        "extensions": argv.extension,
        "search": argv.search,
    }

    if(not argv.path):
        print("Please enter a valid path to start searching. Such as ./")
        exit(1)

    if(argv.min_file_size):
        if(isFileSize(argv.min_file_size)):
            conditions["minimum_size"] = convert_to_byte(argv.min_file_size)
        else:
            raise ValueError("Invalid value provided for --min-size")

    if(argv.min_file_size ):
        if(isFileSize(argv.max_file_size)):
            conditions["maximum_size"] = convert_to_byte(argv.max_file_size)
        else:
            raise ValueError("Invalid value provided for --max-size")

    return conditions


def break_line(text, max_line_length):
    if(len(text) > 0 and max_line_length > 0):
        line_nums = ceil(len(text)/max_line_length)
        lines = []
        for line in range(0, line_nums):
            start_index = line*max_line_length
            lines.append(text[start_index:start_index+max_line_length])
        return linesep.join(lines)
    return text


def convert_bytes_to_readable_unit(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


def convert_to_byte(size):
    result = re.search('(\d+\.?\d*)(b|kb|mb|gb|tb)', size.lower())
    if(result and result.groups()):
        unit = result.groups()[1]
        amount = float(result.groups()[0])
        index = ['b', 'kb', 'mb', 'gb', 'tb'].index(unit)
        return amount * pow(1024, index)
    raise ValueError("Invalid size provided, value is "+size)
    