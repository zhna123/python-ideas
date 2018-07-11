#!/usr/bin/env python
import sys
import re

# python script to count words from a given file

# Assumptions
# 1. words are all alphabet characters
# 2. 2. abbreviated version of words such as 's, 're, Mr. will be treated as ' or . being replaced with an empty char
# 3. case sensitive
# 4. small file size and stored on a single machine


def print_usage():
    print("USAGE: python word_count.py <file_name>")

if len(sys.argv) != 2:
    print_usage()
    sys.exit(0)

word_count = {}
regex = re.compile('[^a-zA-Z\\s]')
with open(sys.argv[1], 'r+') as f:
    file = f.read()
    file = regex.sub('', file)
    for word in file.split():
        if len(word) == 0:
            continue
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
for word in word_count.keys():
    print("%s %s " % (word_count[word], word))