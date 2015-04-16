# Video File Renamer #
Author: Alex Morrison

A python script to rename TV show seasons for Plex.

Renames `.avi` and `.AVI` files into the format `S12E23.avi` for single episodes and `S12E34-E56.avi` for multiple conjoined episodes in one file.

By default, works in current directory, but a target path can be set with the `--path` flag. Note that the script ignores files and folders beginning with a full stop (UNIX hidden).
