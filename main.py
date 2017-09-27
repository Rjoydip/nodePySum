#!/usr/bin/env python

"""
Main py file
"""
import sys
import json
import numpy as np

# Read data from stdin


def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])


def main():
    lines = read_in()

    # create a numpy array
    np_lines = np.array(lines)

    # use numpys sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)

    # return the sum to the output stream
    print lines_sum


# start process
if __name__ == '__main__':
    main()
