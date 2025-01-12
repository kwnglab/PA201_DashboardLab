import pandas as pd
import os

# 프로젝트 경로 가져오기(현재경로의 상위상위폴더)
project_path = "C:/Users/rldnd/DataspellProjects/PA201_DashboardLab"
print(project_path)
ibmhr_path = os.path.join(project_path, 'data', 'interim','ibmhr.xlsx')
ibmhr = pd.read_excel(ibmhr_path)

# 필요한 데이터만 추출
ibmhr =ibmhr[['연령', '퇴직여부', '본부', '출퇴근거리', '교육', '전공', '사원번호',
              '성별', '직무', '결혼여부', '월급', '이직횟수', 'OT여부', '성과평가',
              '총경력년수', '근속년수', '부서']]
# 한국 급여단위로 환산
ibmhr = ibmhr.reset_index(drop=True) # 우선 인덱스를 초기화해야함
ibmhr['d_월급'] = ibmhr['월급'] / 10


## 임의의 데이터 생성
from faker import Faker
import random

# 랜덤 시드 설정
random.seed(240929)
Faker.seed(240929)

# Faker 객체 생성
fake = Faker(locale = 'ko_KR')

fake_list = {
    '성명' : [fake.name() for _ in range(len(ibmhr))],
    '퇴직일자' : [fake.date_between(start_date = '-10y',
                                end_date = pd.to_datetime('2024-12-31')) for _ in range(len(ibmhr))]
}
fake_df = pd.DataFrame(fake_list)
fake_df['퇴직일자'] = pd.to_datetime(fake_df['퇴직일자'])
ibmhr = pd.merge(ibmhr, fake_df, left_index=True, right_index=True)

# 근속일수에 +- 100일 정도의 랜덤 숫자를 더해주어 현실성 증가시켜주고,
# 근속년수는 위 새로운 근속일수에서 다시 구해주는 형태로 변경
ibmhr['d_근속일수'] = (ibmhr['근속년수'] * 365) + random.randint(-100, 100)
ibmhr['d_근속년수'] = round(ibmhr['d_근속일수'] / 365.2425, 1)
ibmhr['d_근속일수'] = pd.to_timedelta(ibmhr['d_근속일수'], unit='D')
ibmhr['입사일자'] = ibmhr['퇴직일자'] - ibmhr['d_근속일수']

# 데이터를 엑셀파일로 변환
ibmhr.to_excel(project_path + "/data/processed/ibmhr.xlsx", index=False)
