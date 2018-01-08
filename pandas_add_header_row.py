#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['grade', 'company_size']
data_frame = pd.read_csv(input_file, header=None, names=header_list)
      # header = None 설정 후 names 변수로 헤더 리스트를 지정해준다

data_frame.to_csv(output_file, index=False)
