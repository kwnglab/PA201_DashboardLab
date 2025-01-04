# %%
import os

import pandas as pd

# 현재 폴더 경로
current_path = os.getcwd()

# 상위 폴더 경로
project_path = os.path.dirname(current_path)
# %%
import kagglehub

# Download latest version
ibm_path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")

print(os.listdir(ibm_path))
ibm_raw = pd.read_csv(ibm_path + "/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Translation of column names to Korean
translated_columns = [
    "나이", "이직 여부", "출장 빈도", "일일 급여", "부서", "집에서의 거리", "교육 수준", "전공 분야", "직원 수", "직원 번호",
    "근무 환경 만족도", "성별", "시급", "업무 몰입도", "직급", "직무", "직무 만족도", "결혼 여부", "월급", "월별 급여",
    "근무한 회사 수", "18세 이상 여부", "초과 근무 여부", "급여 인상률", "성과 등급", "관계 만족도", "표준 근무 시간",
    "주식 옵션 수준", "총 근무 연수", "연간 교육 횟수", "일과 삶의 균형", "회사 근속 연수", "현재 역할 근속 연수",
    "마지막 승진 이후 연수", "현재 관리자와의 근속 연수"
]

# Apply the translated column names to the ibm_rawFrame
ibm_raw.columns = translated_columns

# Define a mapping for translation
translation_dict = {
    "이직 여부": {"Yes": "예", "No": "아니오"},
    "출장 빈도": {"Travel_Rarely": "가끔 출장", "Travel_Frequently": "자주 출장", "Non-Travel": "출장 없음"},
    "부서": {"Sales": "영업", "Research & Development": "연구개발", "Human Resources": "인사"},
    "전공 분야": {
        "Life Sciences": "생명 과학", "Other": "기타", "Medical": "의료",
        "Marketing": "마케팅", "Technical Degree": "기술 학위", "Human Resources": "인사"
    },
    "성별": {"Female": "여성", "Male": "남성"},
    "직무": {
        "Sales Executive": "영업 간부", "Research Scientist": "연구 과학자",
        "Laboratory Technician": "실험실 기술자", "Manufacturing Director": "제조 책임자",
        "Healthcare Representative": "의료 대표", "Manager": "관리자",
        "Sales Representative": "영업 사원", "Research Director": "연구 책임자",
        "Human Resources": "인사"
    },
    "결혼 여부": {"Single": "미혼", "Married": "기혼", "Divorced": "이혼"},
    "18세 이상 여부": {"Y": "예"},
    "초과 근무 여부": {"Yes": "예", "No": "아니오"}
}

# Apply translations to the ibm_rawset
for column, mapping in translation_dict.items():
    ibm_raw[column] = ibm_raw[column].replace(mapping)

print(ibm_raw.head())

# %%
ibm_raw.write_excel(project_path + "/ibm_raw/interim/ibm_raw.xlsx")
