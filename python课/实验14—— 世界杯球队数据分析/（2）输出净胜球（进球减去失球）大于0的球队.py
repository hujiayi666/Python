import pandas as pd

def net_goals_positive_teams():
    """
    输出净胜球（进球减去失球）大于0的球队。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv",encoding="GBK")
    net_goals_positive = data[data["进球"] - data["失球"] > 0]['球队']
    return net_goals_positive

if __name__ == "__main__":
    teams = net_goals_positive_teams()
    print("净胜球大于0的球队：")
    print(teams)