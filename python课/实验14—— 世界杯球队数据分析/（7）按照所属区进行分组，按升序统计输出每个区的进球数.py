import pandas as pd

def group_and_sort_region_goals():
    """
    按照所属区进行分组，按升序统计输出每个区的进球数。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv",encoding="GBK")
    grouped_region_goals = data.groupby("所属洲")['进球'].sum().sort_values(ascending=True)
    return grouped_region_goals

if __name__ == "__main__":
    region_goals = group_and_sort_region_goals()
    print("按照所属区统计的进球数（升序）：")
    print(region_goals)