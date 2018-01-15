#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 헤더 추가하기

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['grade', 'company_size']
        filewriter.writerow(header_list)
        print(header_list)
        for row in filereader:
            filewriter.writerow(row)