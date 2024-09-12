import matplotlib.pyplot as plt
import pandas as pd

from week2 import task1

# 가정된 데이터프레임: Daily Logarithmic Returns
# df['nvda_returns'], df['goog_returns']에 일일 로그 수익률이 저장되어 있어야 합니다.
# 데이터프레임의 결측값 제거
df = task1.df.dropna()

# 수익률 및 리스크 계산
returns = [df['nvda_returns'].mean(), df['goog_returns'].mean()]
risks = [df['nvda_returns'].std(), df['goog_returns'].std()]

# 포트폴리오 통계 정보 생성
portfolio_stats = pd.DataFrame([returns, risks])
portfolio_stats.index = ['returns', 'risks']
portfolio_stats.columns = ['nvda', 'goog']

# 일일 무위험 수익률(risk-free rate) 설정 (1년 영업일 수를 252일로 가정)
risk_free_rate = 0.05 / 252  # 연간 5%의 무위험 수익률을 일간 수익률로 변환

# 비율 설정: 0에서 1까지의 범위 (y=0, y=1)
proportion = [0, 1]


# CAL 계산 함수 정의
def cal_points(risk_free_rate, mean_return, risk, Y_values):
    cal_return = []
    sigma_c = []

    # 각 비율에 대해 CAL 포인트 계산
    for Y in Y_values:
        cal_return.append(risk_free_rate + Y * (mean_return - risk_free_rate))
        sigma_c.append(Y * risk)

    return cal_return, sigma_c


# NVDA 및 GOOG의 CAL 포인트 계산
cal_nvda, sigma_nvda = cal_points(risk_free_rate, portfolio_stats.loc['returns', 'nvda'],
                                  portfolio_stats.loc['risks', 'nvda'], proportion)
cal_goog, sigma_goog = cal_points(risk_free_rate, portfolio_stats.loc['returns', 'goog'],
                                  portfolio_stats.loc['risks', 'goog'], proportion)

# 결과 출력
print(f"Nvidia의 expected return의 범위 : {cal_nvda},\n Nvidia의 risk의 범위 : {sigma_nvda}")
print(f"Google의 expected return의 범위 : {cal_goog},\n Google의 risk의 범위 : {sigma_goog}")

# CAL 그래프 시각화
plt.figure(figsize=(10, 6))

# Nvidia의 CAL 시각화
plt.plot(sigma_nvda, cal_nvda, label='CAL with NVIDIA', color='blue', marker='o')

# Google의 CAL 시각화
plt.plot(sigma_goog, cal_goog, label='CAL with Google', color='green', marker='o')

# 그래프 제목과 라벨
plt.title('Capital Allocation Lines (CAL)')
plt.xlabel('Standard Deviation (Risk)')
plt.ylabel('Expected Return')

# 범례와 그리드 추가
plt.legend()
plt.grid(True)

# 그래프 출력
plt.show()
