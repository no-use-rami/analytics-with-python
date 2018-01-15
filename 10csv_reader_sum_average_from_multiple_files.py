#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.11 파일에서 데이터 값의 합계 및 평균 계산하기

import csv
import glob
import os

import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

output_header_list = ['file_name', 'total', 'average']

csv_out_file = open(output_file, 'a', newline ='')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'deals*')):
    with open(input_file, 'r', newline ='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total = 0.0
        number_of_deals = 0.0
        for row in filereader:
            deal_amount = row[3]
            total += float(deal_amount)
            number_of_deals += 1.0
        average_deals = '{0:.2f}'.format(total/number_of_deals)
        output_list.append(total)
        output_list.append(average_deals)
        filewriter.writerow(output_list)
csv_out_file.close()

