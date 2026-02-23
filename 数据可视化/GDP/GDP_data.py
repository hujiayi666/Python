import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_gdp_data_with_requests():
    base_url = "https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=all&start=1978&end=2023"
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # 检查状态码，如果不是200系列，会抛出异常
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到包含数据的表格元素，根据实际网页结构调整选择器
        table = soup.find('table', {'class': 'views-table'})
        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:  # 跳过表头行
            cols = row.find_all('td')
            country = cols[0].text.strip()
            values = [col.text.strip() for col in cols[1:]]
            data.append([country] + values)
        columns = ['Country'] + [str(year) for year in range(1978, 2024)]
        df = pd.DataFrame(data, columns=columns)
        return df
    except requests.RequestException as e:
        print(f"请求数据时出错: {e}")
    except Exception as e:
        print(f"解析数据时出错: {e}")

if __name__ == "__main__":
    gdp_data = get_gdp_data_with_requests()
    if gdp_data is not None:
        print(gdp_data.head())