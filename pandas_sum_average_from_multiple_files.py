#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2.11.2 팬더스

import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'deals*'))

all_data_frames = []

for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    
    total = pd.DataFrame([float(value) for value in data_frame.loc[:, 'amount']]).sum()
    average = pd.DataFrame([float(value) for value in data_frame.loc[:, 'amount']]).mean()
    
    data = {'file_name': os.path.basename(input_file),
            'total':total,
            'average':average}
    
    all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total', 'average']))

data_frames_concat = pd.concat(all_data_frames, axis = 0, ignore_index = True)
data_frames_concat.to_csv(output_file, index=False)