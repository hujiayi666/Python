import pandas as pd

def qualified_teams():
    """
    输出进球数超过平均数且被罚黄牌少于5张的球队及其进球数和黄牌数。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv",encoding="GBK")
    average_goals = data['进球'].mean()
    qualified_teams_data = data[(data['进球'] > average_goals) & (data['黄牌'] < 5)][['球队', '进球', '黄牌']]
    return qualified_teams_data

if __name__ == "__main__":
    teams_data = qualified_teams()
    print("进球数超过平均数且被罚黄牌少于5张的球队及其进球数和黄牌数：")
    print(teams_data)