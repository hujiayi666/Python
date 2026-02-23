import pandas as pd

def high_goal_success_rate_teams():
    """
    输出进球成功率（进球数/射门数）超过10%的球队及其进球数和射门数。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv",encoding="GBK")
    data['进球成功率'] = data['进球'] / data['射门']
    high_success_rate_teams_data = data[data['进球成功率'] > 0.1][['球队', '进球', '射门']]
    return high_success_rate_teams_data

if __name__ == "__main__":
    teams_data = high_goal_success_rate_teams()
    print("进球成功率超过10%的球队及其进球数和射门数：")
    print(teams_data)