#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'deals_*'))

all_data_frames = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None) # index 열을 지정하지 않는다
    all_data_frames.append(data_frame)
data_frame_cancat = pd.concat(all_data_frames, axis=0, ignore_index=True)
'''pd.concat(objs,  # Series, DataFrame, Panel object
             axis=0,  # 0: 위+아래로 합치기, 1: 왼쪽+오른쪽으로 합치기
             join='outer', # 'outer': 합집합(union), 'inner': 교집합(intersection)
             join_axes=None, # axis=1 일 경우 특정 DataFrame의 index를 그대로 이용하려면 입력
             ignore_index=False,  # False: 기존 index 유지, True: 기존 index 무시
             keys=None, # 계층적 index 사용하려면 keys 튜플 입력
             levels=None,
             names=None, # index의 이름 부여하려면 names 튜플 입력
             verify_integrity=False, # True: index 중복 확인
             copy=True) # 복사 '''
data_frame_cancat.to_csv(output_file, index = False)

# merge() 함수를 통해 SQL join처럼 키가 되는 열을 기준으로 합칠 수 있음
''' pd.merge(dataframe1, dataframe2, on='key', how='inner')'''

# numpy 모듈도 수직 및 수평으로 합치는 기능 제공
# ex) import numpy as np
'np.concatnate([array1, array2], axis=0), np.vstack((array1, array2)), np.r_[array1, array2]' # 수직
'np.concatnate([array1, arrya2], axis=1), np.hstack((array1, array2)), np.c_[array1, array2]' # 수평

 