#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)

# dataframe 형식은 리스트의 목록을 '표' 형태로 저장하는 방식이다.

# read_csv()
# to_csv()
# 두 가지 유용한 함수
