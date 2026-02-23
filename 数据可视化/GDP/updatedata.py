import requests
import pandas as pd
from tqdm import tqdm

# Function to fetch GDP data from World Bank API
def fetch_gdp_data(country_code, start_year, end_year):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD"
    params = {
        "format": "json",
        "date": f"{start_year}:{end_year}",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            return data[1]  # Return the actual data array
    return []

# Function to update the DataFrame with fetched data
def update_gdp_data(df, start_year, end_year):
    years = [str(year) for year in range(start_year, end_year + 1)]
    for year in years:
        if year not in df.columns:
            df[year] = None  # Add missing year columns

    for i, row in tqdm(df.iterrows(), total=len(df), desc="Updating GDP data"):
        country_code = row['USA']  # Adjusted to use the correct column
        fetched_data = fetch_gdp_data(country_code, start_year, end_year)
        for entry in fetched_data:
            year = entry['date']
            gdp_value = entry['value']
            if year in df.columns:
                df.at[i, year] = gdp_value
    return df

# Load the CSV file
file_path = 'C:\\Users\\hujia\\Downloads\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_422027.csv'
data = pd.read_csv(file_path, skiprows=4)

# Focus on years 2019 to 2023
data = update_gdp_data(data, 2019, 2023)

# Save the updated DataFrame
data.to_csv('C:\\Users\\hujia\\Downloads\\Updated_GDP_Data.csv', index=False)
print("Data updated and saved as 'C:\\Users\\hujia\\Downloads\\Updated_GDP_Data.csv'")