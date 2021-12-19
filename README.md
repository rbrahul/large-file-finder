## Large file finder

Sometimes it's very hard to find if some giant files are eating up your system storage. We might need to hunt those down. This simple CLI application helps you to find those giant files that are eating up your system storage.

## How to install and use?

```shell
pip install large-file-finder
```

Now run the following command to your desired path.

```shell
large-file-finder ./
```

## Requirements:

Python 3.4 or later versions need to be installed


### Availble cli arguments:

```shell
large-file-finder -h
```

```
positional arguments:
  path                  relative path where you want to start search. For example ./

optional arguments:
  -h, --help            show this help message and exit
  --limit LIMIT, -limit LIMIT, -l LIMIT
                        Number of files you want to see in the table. Default value is 10. Maximum accepted value is 200
  --min-size MIN_FILE_SIZE, -min-size MIN_FILE_SIZE
                        Minimum file size to search. Accepted values are b, KB, MB, TB. For example --min_file_size 10KB
  --max-size MAX_FILE_SIZE, -max-size MAX_FILE_SIZE
                        Maximum file size to search. Accepted values are b, KB, MB, TB. For example --max_file_size 10KB
  --search SEARCH, -search SEARCH, -s SEARCH
                        Search by name. --search 'my_file.png'
  --hide-limited-access HIDE_LIMITED_ACCESS, -hide-limited-access HIDE_LIMITED_ACCESS
                        Hide the table that contains directories with no access right. Only true or false are accepted
  --extension [EXTENSION ...], -ext [EXTENSION ...]
                        Extension of file such as .txt, .jpeg, .png, .mp3. Multiple extensions are accepted. Such as --extension .txt .png

```

##  File Search result ui

![Large file finder](https://raw.githubusercontent.com/rbrahul/large-file-finder/master/screenshot.png "Large file finder cli application")



## Lisence 

[MIT](https://github.com/rbrahul/gofp/blob/master/LICENSE.md)