import pandas as pd
from sqlalchemy import create_engine

# MySQL database connection settings
db_username = 'root'
db_password = 'root'
db_host = 'localhost'
db_port = '3306'
db_name = 'study_db'
# Connect to MySQL database
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

def preprocess_data(df):
    strings_to_replace = ["", "", ""]
    df.replace(strings_to_replace, "", inplace=True)
    return df

def import_data_to_mysql(file_path):
    file_name = file_path.split('/')[-1].split('.')[0]
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    #df = preprocess_data(df)
    df.to_sql(name=file_name, con=engine, if_exists='replace', index=False)

# Example usage
file_path = 'docs/YourData.csv'
import_data_to_mysql(file_path)