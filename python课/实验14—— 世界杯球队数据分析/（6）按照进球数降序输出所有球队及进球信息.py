import pandas as pd

def sort_teams_by_goals_desc():
    """
    按照进球数降序输出所有球队及进球信息。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv",encoding="GBK")
    sorted_data = data.sort_values(by='进球', ascending=False)[['球队', '进球']]
    return sorted_data

if __name__ == "__main__":
    sorted_teams = sort_teams_by_goals_desc()
    print("按照进球数降序的球队及进球信息：")
    print(sorted_teams)