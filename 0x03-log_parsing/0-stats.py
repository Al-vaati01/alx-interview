#!/usr/bin/python3
"""
log parser
"""
import sys
import re


def check_format(input):
    """
    check format
    """
    g1 = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    g2 = r" - \[(.*?)\] "
    g3 = r"\"GET /projects/260 HTTP/1.1\""
    g4 = r" (\d{3}) (\d+)"
    pattern = r"{}{}{}{}".format(g1, g2, g3, g4)
    match = re.search(pattern, input)
    if match:
        return match
    return None


Total_File_Size = 0
Map_of_statuscodes = {}
NumberOfLines = 0
PossibleStatusCodes = [200, 301, 400, 401, 403, 404, 405, 500]

try:
    for line in sys.stdin:
        NumberOfLines += 1
        match = check_format(line)
        if match:
            Total_File_Size += int(match.group(4))
            status_code = int(match.group(3))
            if status_code in PossibleStatusCodes:
                if status_code in Map_of_statuscodes:
                    Map_of_statuscodes[status_code] += 1
                else:
                    Map_of_statuscodes[status_code] = 1
        if NumberOfLines % 10 == 0:
            print("File size: {}".format(Total_File_Size))
            for key in sorted(Map_of_statuscodes.keys()):
                print("{}: {}".format(key, Map_of_statuscodes[key]))
except KeyboardInterrupt:
    print("File size: {}".format(Total_File_Size))
    for key in sorted(Map_of_statuscodes.keys()):
        print("{}: {}".format(key, Map_of_statuscodes[key]))
