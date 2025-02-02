rule all:
    input:
        "data/interim/ibmhr_translated.xlsx",
        "data/processed/ibmhr.xlsx"

rule translate_data:
    input:
        "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    output:
        "data/interim/ibmhr_translated.xlsx"
    script:
        "src/ibmhr/translate_data.py"


rule preparation_data:
    input:
        "data/interim/ibmhr_translated.xlsx"
    output:
        "data/processed/ibmhr.xlsx"
    script:
        "src/ibmhr/prep_data.py"


