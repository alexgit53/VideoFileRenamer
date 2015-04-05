## Renames Friends Seasons. Probably won't work on anything else ever.

import os
import re

regex = re.compile("S\d+E\d+(-E\d+)?\.[aA][vV][iI]")

# Iterate over files in folder
for root, dirs, files in os.walk("."):
    for filename in files:
        # Check they're a video file, and not already formatted correctly
        if filename.endswith((".avi", ".AVI")) and not regex.match(filename):
            # Extract all the digit sequences from them
            digits = re.findall("\d+", filename)
            nums = [int(s) for s in digits]
            # If there are 2 or more, assume that the first is the series number
            # and all subsequent numbers are episodes
            if len(nums) >= 2:
                newfilename = "S" + '{0:02d}'.format(nums[0]) + "E" + '{0:02d}'.format(nums[1])
                # If there is more than one episode number, make the file name a range
                if len(nums) > 2 and nums[-1] > nums[1]:
                    newfilename += ("-E" + '{0:02d}'.format(nums[-1]))
                print("Renaming " + filename + " to " + newfilename + ".avi")    
                os.rename(os.path.join(root, filename), os.path.join(root, newfilename + ".avi"))
