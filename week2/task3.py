from week2.task2 import portfolio_stats, risk_free_rate

# 무위험 수익률을 사용한 reward-to-variability ratio 계산
S_nvda = (portfolio_stats.loc['returns', 'nvda'] - risk_free_rate) / portfolio_stats.loc['risks', 'nvda']
S_goog = (portfolio_stats.loc['returns', 'goog'] - risk_free_rate) / portfolio_stats.loc['risks', 'goog']

# 결과 출력
print('NVIDIA의 Sharpe Ratio:', S_nvda)
print('Google의 Sharpe Ratio:', S_goog)

'''
NVIDIA는 Google보다 더 높은 샤프 비율을 나타내므로, 동일한 리스크에 대해 더 나은 수익을 얻을 수 있음을 의미합니다.
따라서 투자자는 샤프 비율이 높은 NVIDIA의 포트폴리오를 선택하는 것이 더 효율적입니다.
이는 위험을 감수하는 투자자에게 더 나은 보상을 제공할 수 있는 가능성을 시사합니다.
'''
