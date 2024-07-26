# de-stash-git_changes

An utilty from de-stash collection to watch if there are any changes in the git repository and notify the user about that. Goes well with de-stash-send2tg utility.

**Why do you need it?** \
Sometimes you have a public website (like WordPress or Simple Machine Forum), which are pretty vulnerable to hacking. A good idea is to put the source code under version control (git) to track changes. Besides, you can't update source code every day, but you want to know if there are any changes in the files. This utility will help you to monitor the changes in the git repository and notify you about them.


## Installation

1. Download the script: \
`wget https://github.com/errmakov/de-stash-git_changes/raw/master/de-stash-git_changes.py ` \
or save by link: [de-stash-git_changes.py](https://github.com/errmakov/de-stash-git_changes/raw/master/de-stash-git_changes.py)
2. Make sure Python 3 is installed: `python3 --version`
2. Not installed? Install it: [python.org](https://python.org) or using package manager: `sudo apt install python3`
3. Make sure de-stash-git_changes.py is executable: `chmod +x de-stash-git_changes.py` 

## Usage
Options:
   ```
   --exclude=PATHS Exclude specified paths (separated by semicolons) 
   --dist=DIR Specify the destination directory (mandatory)
   --instance=ID Specify an optional instance identifier
   --o Output "No changes" message if no changes are detected
   -?, -h, --help Show this help message and exit
   ```
Examples:
```
./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site 
./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site --instance=myId 
./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site --o 
./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site --instance=myId --o
``` 

## Usage with de-stash-send2tg
*tbc*
