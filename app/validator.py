import re
from os import sep

def isFileSize(value):
    if(not value):
        return False
    pattern = re.compile("\d+\.?\d*(b|kb|mb|gb|tb)")
    return bool(pattern.fullmatch(value.lower()))


def haveFileConditionsMet(file, options):
    stat = file.stat()
    file_path = str(file)
    path_list = file_path.split(sep)
    file_name = path_list[-1:]

    if(len(options['extensions']) and file.suffix not in options['extensions']):
        return False

    if(options["search"] and not re.search(re.compile(options["search"].lower()),str(file_name).lower())):
        return False

    if(options["minimum_size"] > 0 and stat.st_size < options["minimum_size"]):
        return False

    if(options["maximum_size"] > 0 and stat.st_size > options["maximum_size"]):
        return False

    return True
