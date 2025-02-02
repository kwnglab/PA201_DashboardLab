println("hello world αβγ")

########################
# Pakcage를 설치하는 방법
########################
# using Pkg
# Pkg.add("Plots")
# Pkg.add("CSV")
# Pkg.add("DataFrames")
# Pkg.add("PyCall")
# Pkg.add("JLD2")

# Package 모드를 빨리 들어가는 법
# ] <- package mode로 들어감
# Backspace <- package mode에서 나감

# Function을 사용하는 방법
function hello()
    println("hello world")
end

# # 결측치
# nothing은 원래 없는 것
# missing은 '있어야 할' 데이터가 없는 것

using CSV
using DataFrames
using XLSX

current_path = dirname(dirname(@__DIR__))
println(current_path)

# CSV 파일을 DataFrame으로 변환
df_raw = CSV.File(joinpath(current_path, "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")) |> DataFrame

# 엑셀 파일을 DataFrame으로 변환
df_kor = XLSX.readtable(joinpath(current_path, "data/processed/ibmhr.xlsx"), "Sheet1") |> DataFrame

# Column name 보는 법
println(propertynames(df_kor))


describe(df_kor)

using StatsBase
unique(df_kor.퇴직여부)
countmap(df_kor.퇴직여부)
