import os
import pandas as pd

# 경로
current_path = os.getcwd()

# 상위 폴더 경로
project_path = os.path.dirname(current_path) + "/PA201_DashboardLab"


# 캐글허브에서 IBM HR 데이터 다운로드
import kagglehub

# Download latest version
ibm_path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")

print(os.listdir(ibm_path))
ibmhr = pd.read_csv(ibm_path + "/WA_Fn-UseC_-HR-Employee-Attrition.csv")

ibmhr.rename(columns={
    'Age': '연령',
    'Attrition': '퇴직여부',
    'BusinessTravel': '출장빈도',
    'DailyRate': '일일요금',
    'Department': '부서',
    'DistanceFromHome': '출퇴근거리',
    'Education': '교육',
    'EducationField': '전공',
    'EmployeeCount': '사원수',
    'EmployeeNumber': '사원번호',
    'EnvironmentSatisfaction': '환경만족도',
    'Gender': '성별',
    'HourlyRate': '시간당급여',
    'JobInvolvement': '직무몰입도',
    'JobLevel': '직급',
    'JobRole': '직무',
    'JobSatisfaction': '직무만족도',
    'MaritalStatus': '결혼여부',
    'MonthlyIncome': '월급',
    'MonthlyRate': '월요금',
    'NumCompaniesWorked': '이직횟수',
    'Over18': '성인여부',
    'OverTime': 'OT여부',
    'PercentSalaryHike': '급여인상률',
    'PerformanceRating': '성과평가',
    'RelationshipSatisfaction': '관계만족도',
    'StandardHours': '소정근무시간',
    'StockOptionLevel': '스톡옵션',
    'TotalWorkingYears': '총경력년수',
    'TrainingTimesLastYear': '지난해훈련횟수',
    'WorkLifeBalance': '일생활균형',
    'YearsAtCompany': '근속년수',
    'YearsInCurrentRole': '현직무근무년수',
    'YearsSinceLastPromotion': '현직급근무년수',
    'YearsWithCurrManager': '현직책근무년수'
},
    inplace=True)


# 밸류 번역
translation_dict = {
    "퇴직여부": {"Yes": "예", "No": "아니오"},
    "출장빈도": {"Travel_Rarely": "가끔 출장", "Travel_Frequently": "자주 출장", "Non-Travel": "출장 없음"},
    "부서": {"Sales": "영업", "Research & Development": "연구개발", "Human Resources": "인사"},
    "전공": {
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
    "결혼여부": {"Single": "미혼", "Married": "기혼", "Divorced": "이혼"},
    "성인여부": {"Y": "예"},
    "OT여부": {"Yes": "예", "No": "아니오"}
}

# Apply translations to the ibm_rawset
for column, mapping in translation_dict.items():
    ibmhr[column] = ibmhr[column].replace(mapping)

# 직무에 따른 부서 세분화
ibmhr = ibmhr.rename(columns={"부서": "본부"})

ibmhr['부서'] = ibmhr['본부']
ibmhr['부서'] = ibmhr.apply(lambda x: "의료연구팀" if (x['직무'] == "연구 과학자") | (x['직무'] == "연구 책임자")
else x['부서'], axis=1)
ibmhr['부서'] = ibmhr.apply(lambda x: "의료제조팀" if (x['직무'] == "제조 책임자") | (x['직무'] == "실험실 기술자")
else x['부서'], axis=1)

# 데이터를 엑셀파일로 변환
ibmhr.to_excel(project_path + "/data/interim/ibmhr.xlsx", index=False)
