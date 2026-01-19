import pandas as pd
import numpy as np
# df=pd.read_csv("./data/raw_trade_data.csv", encoding='utf-8')
# df=pd.read_csv("./data/raw_trade_data.csv", encoding='cp949')

# 과제 1 : [실무형] 특정 품목의 수출입 현황 보고서 준비하기

trade=pd.read_csv("./data/raw_trade_data.csv", encoding='cp949') 
print(trade.head(10))

# 전체 데이터에서 **HS코드 앞 2자리가 '85'**인 데이터만 추출
trade_85=trade[trade["hs_code"].astype(str).str[:2]=="85"]

# 그중 **국가명이 '미국' 혹은 '베트남'**인 데이터만 필터링 isin(['미국', '베트남']) 다중 조건 필터링
trade_85_us_vn=trade_85[trade_85["국가명"].isin(['미국', '베트남'])]

# 수출금액이 없는(0인) 데이터는 분석에서 제외
trade_85_us_vn_nonzero=trade_85_us_vn[trade_85_us_vn["수출금액"]!=0]

# 결과 데이터의 상위 10개를 출력
print(trade_85_us_vn_nonzero.head(10))

# semiconductor_report.csv로 저장
trade_85_us_vn_nonzero.to_csv("./data/semiconductor_report.csv", index=False)

print("====================과제 1 완료====================")
# 과제 2 : [데이터 클렌징] 지저분한 무역 데이터 바로잡기
# 실제 무역 데이터는 단위가 섞여 있거나 오타가 많습니다. 이를 정제하는 과제입니다.

# 시나리오: 시스템 오류로 인해 데이터의 일부가 오염되었습니다. 분석 전 데이터를 정규화해야 합니다.

# '중량' 컬럼에 결측치가 있다면 해당 품목의 평균 중량으로 채우세요. (어려우면 0으로 채우기)
group_mean = trade.groupby('hs_code')['중량'].transform('mean')
trade.loc[trade['중량'].isna(), '중량'] = group_mean[trade['중량'].isna()]

# '수출입구분' 컬럼의 데이터가 영문(Import, Export)으로 되어 있다면 국문(수입, 수출)으로 일괄 변경하세요.
trade.loc[trade['수출입구분'] == 'Import', '수출입구분'] = '수입'
trade.loc[trade['수출입구분'] == 'Export', '수출입구분'] = '수출'

# 현재 '수출금액' 단위가 '원'입니다. 이를 '백만 달러' 단위로 변환한 수출금액_M_USD 컬럼을 만드세요. (환율 1,470원 가정)
trade['수출금액_M_USD'] = trade['수출금액'] / 1470 / 1000000

# 변경 후 데이터의 각 컬럼별 데이터 타입(df.dtypes)을 확인하여 수치형 데이터가 맞는지 검증하세요.
print(trade.dtypes)
print("====================과제 2 완료====================")
