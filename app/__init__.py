
from pathlib import Path
import argparse
from halo import Halo

from app.view import print_directory_with_restricted_access, print_biggest_files
from app.helper import prepare_filter_config
from app.scanner import traverse_dir


def main(argv):
    conditions = prepare_filter_config(argv)

    scanned = []
    permission_issue = []

    path = Path.cwd().joinpath(argv.path).resolve()
    spinner = Halo(text='Scanning files', spinner='bouncingBall', text_color="green")
    spinner.start()
    traverse_dir(path, scanned, permission_issue, conditions)
    spinner.stop()
    print_biggest_files(scanned, argv.limit)

    if(argv.hide_limited_access == 'false'):
        print_directory_with_restricted_access(permission_issue)



def initialize():
    parser = argparse.ArgumentParser(description='An CLI application to find big files in the file system.',)
    parser.add_argument('--limit', '-limit', '-l', type=int,
                        help='Number of files you want to see in the table. Default value is 10. Maximum accepted value is 200', default=15)
    parser.add_argument('--min-size', '-min-size', dest="min_file_size",
                        help='Minimum file size to search. Accepted values are b, KB, MB, TB. For example --min_file_size 10KB')
    parser.add_argument('--max-size', '-max-size', dest="max_file_size",
                        help='Maximum file size to search. Accepted values are b, KB, MB, TB. For example --max_file_size 10KB')
    parser.add_argument('--search', '-search', '-s', help="Search by name. --search 'my_file.png'")
    parser.add_argument('--hide-limited-access', '-hide-limited-access', dest="hide_limited_access", default="false", help='Hide the table that contains directories with no access right. Only true or false are accepted')
    parser.add_argument('--extension', '-ext', default=[], nargs='*',
                        help='Extension of file such as .txt, .jpeg, .png, .mp3. Multiple extensions are accepted. Such as --extension .txt .png')
    parser.add_argument('path', help="relative path where you want to start search. For example ./")
    args = parser.parse_args()
    main(args)
