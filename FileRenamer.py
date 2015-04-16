# Renames .avi file TV shows for Plex (into format S12E34.avi or S12E34-E56.avi for multiple episodes
# Author: Alex Morrison Github: Alexgit53

import os
import re
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path to the directory containing files to rename")
    args = parser.parse_args()

    # File names matching this regex are considered to be correctly formatted (eg S1E3.avi or S4E23-E24.AVI)
    correct_format_regex = re.compile("^S\d+E\d+(-E\d+)?\.(avi|AVI)")
    # File names matching this regex are considered to be video files (ie anything with file extension .avi or .AVI)
    video_file_regex = re.compile("^.*\.(avi|AVI)$")

    if args.path:
        if os.path.exists(args.path):
            target_path = args.path
        else:
            sys.exit("Path does not exist")
    else:
        target_path = "."

    # Iterate over files in current folder
    for root, dirs, files in os.walk(target_path):
        # Exclude UNIX hidden files and directories (those beginning with a ".", eg ".gitignore")
        # This does not skip files on Windows with the hidden attribute
        files = [f for f in files if not f[0] == "."]
        dirs[:] = [d for d in dirs if not d[0] == "."]

        for filename in files:
            # Check they're video files, but not already formatted correctly
            if video_file_regex.match(filename) and not correct_format_regex.match(filename):
                # Extract all the digit sequences from them
                digits = re.findall("\d+", filename)
                nums = [int(s) for s in digits]
                # If there are 2 or more, assume that the first is the series number
                # and all subsequent numbers are episodes
                if len(nums) >= 2:
                    new_filename = "S" + '{0:02d}'.format(nums[0]) + "E" + '{0:02d}'.format(nums[1])
                    # If there is more than one episode number, make the file name a range
                    if len(nums) > 2 and nums[-1] > nums[1]:
                        new_filename += ("-E" + '{0:02d}'.format(nums[-1]))
                    print("Renaming " + filename + " to " + new_filename + ".avi")
                    os.rename(os.path.join(root, filename), os.path.join(root, new_filename + ".avi"))

if __name__ == "__main__":
    main()