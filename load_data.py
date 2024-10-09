import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/hr_dataset.csv')

print("Data from CSV:")
print(df.head())

try:
    engine = create_engine('postgresql+psycopg2://postgres:disha123@127.0.0.1:5432/hr_dash_db')

    with engine.connect() as connection:
        print("Connection successful!")

        df.to_sql('employee', con=engine, if_exists='replace', index=False)

    print("Data loaded successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

