import pandas as pd
import os

# 프로젝트 경로 가져오기(현재경로의 상위상위폴더)
project_path = "C:/Users/rldnd/DataspellProjects/PA201_DashboardLab"
ibmhr = pd.read_excel(project_path + "/data/interim/ibmhr.xlsx")

# 필요한 데이터만 추출
ibmhr =ibmhr[['연령', '퇴직여부', '본부', '출퇴근거리', '교육', '전공', '사원번호',
              '성별', '직무', '결혼여부', '월급', '이직횟수', 'OT여부', '성과평가',
              '총경력년수', '근속년수', '부서']]
# 한국 급여단위로 환산
ibmhr = ibmhr.reset_index(drop=True) # 우선 인덱스를 초기화해야함
ibmhr['d_월급'] = ibmhr['월급'] / 10

# 데이터를 엑셀파일로 변환
ibmhr.to_excel(project_path + "/data/processed/ibmhr.xlsx", index=False)
