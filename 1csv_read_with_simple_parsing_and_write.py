#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys #커맨드라인에 입력된 인수를 스크립트로 넘겨주는 모듈이다

input_file = sys.argv[1]
output_file = sys.argv[2]
# sys.argv[인덱스] 사용할 때 참고
# python [0]스크립트명.py "[1] 파일주소", "[2] 파일주소"

with open(input_file, 'r', newline='') as filereader:
    with open(output_file, 'w', newline='') as filewriter:
      # with문은 종료될 때 자동으로 파일을 닫아줘서 close 함수를 따로 써줄 필요가 없다
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')
              # map()함수는 특정 리스트의 각 원소를 특정 형식(문자열 등)으로 만든다
              # join()함수는 특정 리스트의 각 값 사이에 특정 문자(쉼표 등)를 삽입하고 리스트를 문자열로 변환한다.
              # filewriter 객체는 그 문자열을 출력 파일의 첫 번째 행에 기록한다.
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
              # 나머지 행을 반복한다
              
    
