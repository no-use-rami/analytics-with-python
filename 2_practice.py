#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2장 연습문제

'''
1. 조건, 집합, 또는 정규 표현식에 따라 행을 필터링하는 스크립트 중 하나를 수정하여 예제에서
필터링한 것과 다른 행을 출력하고, 출력 파일을 작성해보라.
'''

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

df1 = pd.read_csv(input_file)
df1_value = df1.loc[(df1['amount'] > 100000000), :]

df1_value.to_csv(output_file, index=False)

# python 2_practice.py "./deals_dec_2017.csv" "2_practice_1.csv"
# deals_dec_2017.csv 파일에서 'amount' 열이 1억 이상인 값만 가져와 작성한다.



'''
2. 인덱스 값 또는 열 헤더를 기반으로 열을 필터링하는 스크립트 중 하나를 수정하여
예제에서 필터링한 것과 다른 열을 출력하고, 출력 파일을 작성해보라.
'''

input_file = sys.argv[1]
output_file = sys.argv[2]


df2 = pd.read_csv(input_file)
#df2_value = df2.iloc[:,1]
df2_value = df2.loc[:, 'title']


df2_value.to_csv(output_file, index=False)

# python 2_practice.py "./deas_dec_2017.csv" "2_practice_2.csv"
# deals_dec_2017.csv 파일에서 인덱스[1] 또는 'title' 칼럼의 데이터를 가져와 작성한다.


'''
3. 우선 폴더에 새로운 CSV 입력 파일들을 만들고, 별도의 출력 폴더를 만든다.
여러 개의 파일을 처리하는 스크립트 중 하나를 사용하여 새로운 입력 파일들을 처리하고
그 결과를 출력 파일로 만들어 해당 출력 폴더에 저장해보라.
'''

import glob
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, '2_practice_3*'))

all_data_frames = []
for file in all_files:
    df3 = pd.read_csv(file, index_col=None)
    all_data_frames.append(df3)
df3_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
df3_concat.to_csv(output_file, index = False)

# python 2_practice.py "./2_practice_3" "2_practice_3.csv"
# 현재 위치에서 하위 2_practice_3 폴더의 2_practice_3*.csv 파일을 모두 읽고 하나로 합쳐 작성한다.