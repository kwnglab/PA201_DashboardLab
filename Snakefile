rule all:
    input:
        "data/interim/ibmhr_translated.xlsx",
        "data/processed/ibmhr.xlsx"

rule download_data:
    output:
        "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    shell:
        """
        python src/ibmhr/download_data.py {output}
        """

rule translate_data:
    input:
        "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    output:
        "data/interim/ibmhr_translated.xlsx"
    shell:
        """
        python src/ibmhr/translate_data.py {input}  {output}
        """

rule preparation_data:
    input:
        "data/interim/ibmhr_translated.xlsx"
    output:
        "data/processed/ibmhr.xlsx"
    shell:
        """
        python src/ibmhr/prep_data.py {input} {output}
        """


