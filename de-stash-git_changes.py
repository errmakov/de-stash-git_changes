#!/usr/bin/env python3

import os
import sys
import subprocess

def print_usage():
    print("""
Usage: monitor_changes.py [OPTIONS]

Options:
  --exclude=PATHS    Exclude specified paths (separated by semicolons)
  --dist=DIR         Specify the destination directory (mandatory)
  --instance=ID      Specify an optional instance identifier
  --o                Output "No changes" message if no changes are detected
  -?, -h, --help     Show this help message and exit

Examples:
  ./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site
  ./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site --instance=myId
  ./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site --o
  ./monitor_changes.py --exclude=/path1;/path2 --dist=/path/to/your/wordpress/site --instance=myId --o
  """)

def run_git_status(exclude_paths, dist_dir):
    # Change to the specified directory
    try:
        os.chdir(dist_dir)
    except FileNotFoundError:
        print(f"Error: The specified directory '{dist_dir}' does not exist{instance_message}.")
        sys.exit(-1)
    except PermissionError:
        print(f"Error: Permission denied for directory '{dist_dir}'{instance_message}.")
        sys.exit(-1)

    # Check if the current directory is a Git repository
    if not os.path.isdir(".git"):
        print(f"Error: The specified directory '{dist_dir}' is not a Git repository{instance_message}.")
        sys.exit(1)

    # Construct the git status command with exclusions
    git_status_cmd = ["git", "status", "--porcelain"]
    try:
        # Run the git status command
        result = subprocess.run(git_status_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result.check_returncode()
    except subprocess.CalledProcessError as e:
        print(f"Error running git status: {e.stderr}")
        sys.exit(1)

    # Filter out the excluded paths from the result
    changes = []
    for line in result.stdout.splitlines():
        if not any(line.startswith(f" {exclude}") for exclude in exclude_paths):
            changes.append(line)

    return changes

def main():
    exclude_paths = []
    dist_dir = ""
    global instance_message
    instance_id = ""
    no_changes_message = False

    # Parse command line arguments
    for arg in sys.argv[1:]:
        if arg in ("-?", "-h", "--help"):
            print_usage()
            sys.exit(0)
        elif arg.startswith("--exclude="):
            exclude_paths = arg[len("--exclude="):].split(";")
        elif arg.startswith("--dist="):
            dist_dir = arg[len("--dist="):]
        elif arg.startswith("--instance="):
            instance_id = arg[len("--instance="):]
        elif arg == "--o":
            no_changes_message = True

    # Check if dist_dir is provided
    if not dist_dir:
        print("Error: --dist option is mandatory.")
        print_usage()
        sys.exit(-1)

    instance_message = f" at {instance_id}" if instance_id else ""

    # Run git status and check for changes
    changes = run_git_status(exclude_paths, dist_dir)

    # Output the result
    if changes:
        print(f"There are uncommitted changes in the repository '{dist_dir}'{instance_message}.")
    elif no_changes_message:
        print(f"No changes in '{dist_dir}'{instance_message}.")

if __name__ == "__main__":
    main()

