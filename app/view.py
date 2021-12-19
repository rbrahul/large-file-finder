
import heapq
from tabulate import tabulate

from app.helper import break_line, convert_bytes_to_readable_unit
from app.constants import MAX_CHAR_LENGTH_PER_LINE, MAX_ROW_COUNT


def print_directory_with_restricted_access(permission_issue):
    if(len(permission_issue) > 0):
        print("\n\033[33m"+tabulate([[break_line(str(item), MAX_CHAR_LENGTH_PER_LINE)] for item in permission_issue], headers=["Index",
              "Could not scan these directories because of limited permission"], showindex="always", tablefmt="fancy_grid"))


def print_biggest_files(scanned, limit=15):
    if(limit > MAX_ROW_COUNT):
        limit = MAX_ROW_COUNT
    largest_files = heapq.nlargest(limit, scanned, key=lambda item: item['size'])
    print("\n\033[32m"+tabulate([[convert_bytes_to_readable_unit(row["size"]), break_line(row["path"], MAX_CHAR_LENGTH_PER_LINE)] for row in largest_files], headers=[
          "Index", "Size", "File Path"], showindex="always", tablefmt="fancy_grid"))
