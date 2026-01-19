import pandas as pd
import numpy as np

dict_data = {"a": 1, "b": 2, "c": 3}
series_data = pd.Series(dict_data)
print(type(series_data))
print(series_data)

list_data = ["2026-01-19", 3.14, "abc", 100, True]
series_data2 = pd.Series(list_data)
print(type(series_data2))
print(series_data2)

dict_data={"c0": [1, 2, 3], "c1": [4, 5, 6], "c2": [7, 8, 9], "c3": [10, 11, 12], "c4": [13, 14, 15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)

# 판다스 데이터 내용 확인
# .columns : 컬럼 명 확인
# .head() : 상위 5개 행 출력
# .tail() : 하위 5개 행 출력 () 내에 숫자 입력 시 해당 개수 출력
# .shape : (행, 열) 크기 확인
# .info() : 데이터 전반적인 정보 제공
# 행과 열의 크기
# 컬럼명
# 컬럼별 결측치
# 컬럼별 데이터 타입
# .type() : 데이터 타입 확인

# 파일 불러오기
# 형식     읽기              쓰기
# csv     read_csv()       to_csv()
# exel    read_excel()     to_excel()
# json    read_json()      to_json()
# html    read_html()      to_html()

# data 폴더에 있는 Titanic-Dataset.csv 파일 읽기, 만약 python 파일이 다른 폴더에 있다면 "../data/Titanic-Dataset.csv"
# ./ 내가 있는 기준으로 하위 폴더 이동
# ../ 내가 있는 기준으로 나가서 상위 폴더 이동
titanic=pd.read_csv("./data/Titanic-Dataset.csv")   
print(titanic)
print(titanic.columns)
print(titanic.head())
print(titanic.tail(10))
print(titanic.shape)
print(titanic.info())

print(type(titanic))

# pandas 에서 특정 열을 선택
# 열 1개 선택 = Series객체 변환
# 데이터 프레임의 열 데이터 1개만 선택할 때 2가지 방식
# 1) 대괄호[] 안에 열 이름을 따옴표로 함께 입력
# 2) 점(.) 다음에 열 이름 입력
# 열 n 개 선택 = DataFrame 객체 변환
# 데이터 프레임의 열 데이터 n개를 선택할때는  1개의 방식
# 이중 대괄호[[]] 안에 열 이름을 따옴표로 입력
# *** 만약 열 1개를 데이터 프레임 객체로 추출하려면 [[]] 사용 가능

names=titanic["Name"]
print(names.head())
names=titanic.Name
print(names.head())
print(type(names))
print(names.shape)

double_columns=titanic[["Sex","Age"]] 
print(double_columns.head())
print(type(double_columns))
print(double_columns.shape) 

# pandas 데이터 필터링

# 1. boolean 인덱싱 True값을 가진 행만 추출
# 2. .isin() 각각의 요소가 데이터 프레임 또는 시리즈에 존재하는지 파악한 후 True/False 반환
# 3. .isna() 결측 값은 True, 결측 값이 아니면 False 반환
# 4. .notna() 결측 값이 아니면 True, 결측 값이면 False 반환

print(double_columns["Age"]>=35)
above35=double_columns["Age"]>=35

above35=double_columns[double_columns["Age"]>=35]
print(above35.head())   # True 값만 필터링

# 성별 남자만 추출
above_male=titanic[titanic["Sex"]=="male"]
print(above_male.head())

print(titanic.head())
class1=titanic[titanic["Pclass"].isin([1])]
print(class1.head())


print(double_columns.head())
age2040=double_columns[double_columns["Age"].isin(np.arange(20,41))]
print(age2040.head())

print(double_columns.head(7))
class_2=double_columns["Age"].isna()
print(class_2.head(7))      # 비어있는 cell True 변환

class_3=double_columns["Age"].notna()
print(class_3.head(7))      # 비어있는 cell False 변환

# 결측값을 제거한 누락되지 않은 값을 확인
# 행 제거

print(double_columns.head(10))
age5=double_columns[double_columns["Age"].notna()]
print(age5.head(10))

# 결측치 제거(없는 값)

# .dropna(axis=0) == .dropna()  # 결측 값들이 들어있는 행 전체 삭제
# .dropna(axis=1)               # 결측 값들이 들어있는 열 전체 삭제

print(titanic.head())
print(titanic.dropna())

print(titanic.dropna(axis=1).head())

# pandas 이름과 인덱스로 특정 행광 열 선택

# .loc[] : 행 이름과 열 이름 사용   DataFrame.loc[행 이름, 열 이름]
# .iloc[] : 행 번호와 열 번호 사용  DataFrame.iloc[행 번호, 열 번호]

name35=titanic.loc[titanic["Age"]>=35, ["Name", "Age"]]
print(name35.head())

name35.iloc[[1,2,3],0]="No name"
print(name35.head())        # 원본은 변경되지 않음

# 판다스 데이터 통계

# .mean() : 평균값
# .median() : 중앙값
# .describe() : 요약 통계량(개수, 평균, 표준편차, 최소값, 4분위수, 최대값)      
            # mean(), std(), min(), 25%, 50%, 75%, max() 포함
# .agg() : 여러개의 열에 다양한 함수 적용
# 모든 열에 여러 함수를 매핑: group.객체.agg(함수1, 함수2, ...)
# 각 열마다 다른 함수를 매핑: group.객체.agg({"열이름1": 함수1, "열이름2": 함수2, ...})
# .groupby() : 그룹 별 집계
# .value_counts() : 값의 개수
print("-------평균 나이-------")
print(titanic["Age"].mean())

print("-------중앙값-------")
print(titanic["Age"].median())

print("-------다양한 통계량 요약-------")
print(titanic.describe())

print("-------나이와 요금의 평균 및 표준 편차-------")
print(titanic[["Age","Fare"]].agg(["mean", "std"]))

print("-------열별 사용자 집계-------")
agg_dict={
    "Age": ["min", "max", "mean"],
    "Fare": ["median", "sum"]
}
print(titanic.agg(agg_dict))

print("-------성별 기준으로 평균 나이 및 요금-------")
print(titanic.groupby("Sex")[["Age","Fare"]].mean())

print("-------객실 등급(Pclass)별 탑승자 수-------")
print(titanic["Pclass"].value_counts())

print("-------성별(Sex)별 탑승자 수-------")
print(titanic["Sex"].value_counts())

print("-------새로운 열 country 생성 USA------")
titanic["country"]="USA"
print(titanic)

print("-------기본의 열을 계산해서 새로운 열을 추가")
titanic["New_Age"]=titanic["Age"]+10
print(titanic)

# 20세 미만이면 child, 아니 면 adult 
print("-------20세 미만이면 child, 아니면 adult -------")
titanic["Age_grop"]="Adult"
titanic.loc[titanic["Age"]<20, "Age_grop"]="Child"
print(titanic)

# 데이터 프레임의 가장 마지막 인덱스 확보 후 행 추가
new_index=len(titanic)
print(new_index)

titanic.loc[new_index]=[992,1,1,"shin","female",53,0,0,"Pc123",50.0,"C123","S","USA",63,"Adult"]
new_data=pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age":[22,30],
    "Sex": ["female","male"],
    "Survived": [1,0]
})

titanic=pd.concat([titanic, new_data], ignore_index=True)
print(titanic.tail())
# titanic["Name"].str.startswith("Sa")          # 문자열이 "Sa"로 시작하는 자료
# titanic["Age"].astype(str).str.startswith("2")  # 문자열로 변환 후 "2"로 시작하는 자료
# titanic["Age"].astype(str).str.startswith("^82")  # 문자열로 변환 후 "82"로 시작하는 자료

# 파일 저장     # ./ 현재 폴더에 저장
titanic.to_csv("./sample.csv" , index=False)
titanic.to_excel("./sample.xlsx" , index=False)
print("파일 저장 완료")