import os
import pandas as pd

def get_project_path():
    current_file_path = os.getcwd()  # 현재 파일의 절대 경로
    path = os.path.dirname(current_file_path)  # 현재 파일의 디렉토리 경로

    # 최상위 폴더로 이동
    while not os.path.isfile(os.path.join(path, 'README.md')):  # 최상위 폴더에 있는 파일 예: README.md
        path = os.path.dirname(path)  # 한 단계 상위 디렉토리로 이동
        if path == '/':
            break  # 루트 디렉토리에 도달하면 중단

    return path

# 함수 호출
project_path = get_project_path()
print("Project Root:", project_path)


# 캐글허브에서 IBM HR 데이터 다운로드
import kagglehub

# Download latest version
ibm_path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")

print(os.listdir(ibm_path))
ibmhr = pd.read_csv(ibm_path + "/WA_Fn-UseC_-HR-Employee-Attrition.csv")
ibmhr.to_csv(project_path + "/data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")
