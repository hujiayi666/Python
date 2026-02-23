import pandas as pd

def red_card_teams():
    """
    输出被罚红牌的球队。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv",encoding="GBK")
    red_card_teams_list = data[data['红牌'] > 0]['球队']
    return red_card_teams_list

if __name__ == "__main__":
    teams = red_card_teams()
    print("被罚红牌的球队：")
    print(teams)