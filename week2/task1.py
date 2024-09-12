import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 데이터 다운로드 기간 설정
start_date = "2024-08-01"
end_date = "2024-08-31"

# yfinance를 사용한 데이터 다운로드
nvda_data = yf.download('NVDA', start=start_date, end=end_date)
goog_data = yf.download('GOOG', start=start_date, end=end_date)

# 사용한 columns만 추출 및 이름 변경
nvda_data = nvda_data.rename(columns={'Close': 'nvda_price'})
goog_data = goog_data.rename(columns={'Close': 'goog_price'})

# 'Close' 열만 사용 (종가)
nvda_data = nvda_data[['nvda_price']]
goog_data = goog_data[['goog_price']]

# 데이터 결합 (NVDA와 GOOG 데이터를 하나로 합침)
df = pd.concat([nvda_data, goog_data], axis=1)

# 중간 데이터를 삭제해 메모리 관리
del nvda_data, goog_data

# Shift를 사용한 daily logarithmic returns 계산
df['nvda_returns'] = np.log(df['nvda_price'] / df['nvda_price'].shift(1))
df['goog_returns'] = np.log(df['goog_price'] / df['goog_price'].shift(1))

# 데이터 크기 및 샘플 출력
print('전체 데이터의 크기 :', df.shape, '\n')
print(df)

# NVDA와 GOOG의 로그 수익률 시각화
plt.figure(figsize=(10,6))

# NVDA 로그 수익률
plt.plot(df.index, df['nvda_returns'], label='NVDA Log Returns', marker='o')

# GOOG 로그 수익률
plt.plot(df.index, df['goog_returns'], label='GOOG Log Returns', marker='o')

# 그래프 제목 및 라벨 설정
plt.title('NVDA vs GOOG Daily Logarithmic Returns (Aug 2024)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Log Returns', fontsize=12)

# 범례 추가
plt.legend()

# X축 날짜 각도 조정
plt.xticks(rotation=45)

# 그래프 표시
plt.tight_layout()
plt.show()

'''
2024년 8월 동안 NVIDIA(NVDA)와 Google(GOOG)의 종가 데이터를 바탕으로 일일 로그 수익률을 계산했습니다.
NVDA는 -0.065978에서 0.063265 사이의 변동성을 보였고, GOOG는 -0.047176에서 0.021974 사이에서 변동하였습니다.
이를 통해 두 주식의 단기 변동성을 비교할 수 있었으며, NVDA가 GOOG보다 더 높은 변동성을 가졌음을 확인할 수 있었습니다.
'''
