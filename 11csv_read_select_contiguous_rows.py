#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

row_counter = 0
with open(input_file, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 8:
                print(row_counter, [value.strip() for value in row])
                filewriter.writerow([value.strip() for value in row])
                      # value.strip()은 또 어디서 온 걸까
            row_counter += 1

