import excel "C:\Users\kwng\DataspellProjects\PA201_DashboardLab\data\processed\ibmhr.xlsx", sheet("Sheet1") firstrow clear

collapse (count) 사원번호 (mean) 연령, by(전공)
encode 전공, gen(전공cd)
dtable i.전공 연령