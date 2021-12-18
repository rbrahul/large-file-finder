## 💻 Big file finder

A CLI application to locate big files in your file system. I wrote these code from my personal necessity. Thought someone else might need it as well. Here you go..

## How to run?

```shell
python ./main.py ./ --limit=25 --min-size=50mb --max-size=60gb 
```

#### CLI argumment:

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

##  File Search result

╒═════════╤══════════╤══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╕
│   Index │ Size     │ File Path                                                                                                                │
╞═════════╪══════════╪══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
│       0 │ 59.6 GB  │ /Users/john.doe/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw                                      │
├─────────┼──────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│       1 │ 2.6 GB   │ /Users/john.doe/Downloads/Jenkins Tutorial For Beginners/Jenkins Tutorial For Beginners.zip                          │
├─────────┼──────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│       2 │ 726.2 MB │ /Users/john.doe/Downloads/[ FreeCourseWeb.com ] Udemy - Helm Masterclass.zip                                         │
├─────────┼──────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│       3 │ 502.1 MB │ /Users/john.doe/.minikube/cache/preloaded-tarball/preloaded-images-k8s-v11-v1.21.2-docker-overlay2-amd64.tar.lz4     │
├─────────┼──────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│       4 │ 361.1 MB │ /Users/john.doe/.minikube/cache/kic/kicbase_v0.0.25@sha256_6f936e3443b95cd918d77623bf7b595653bb382766e280290a02b4a34 │
│         │          │ 9e88b79.tar                                                                                                              │
╘═════════╧══════════╧══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╛
