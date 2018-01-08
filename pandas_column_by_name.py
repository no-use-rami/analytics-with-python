#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['grade', 'company_size']]

data_frame_column_by_name.to_csv(output_file, index=True)