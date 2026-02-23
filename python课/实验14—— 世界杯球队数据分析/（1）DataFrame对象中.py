import pandas as pd

def read_data():
    """
    利用pandas库的read_csv()函数读取“2018世界杯球队数据.csv”中的数据，并存入一个DataFrame对象中。
    """
    data = pd.read_csv(r"D:\cxdownload\实验14资料\2018世界杯球队数据.csv", encoding='GBK')
    return data

if __name__ == "__main__":
    df = read_data()
    print(df.head(10))  # 打印前10行数据查看读取情况，可按需删除此行