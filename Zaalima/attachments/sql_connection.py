import sqlite3
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO,filename='test.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')


logger = logging.getLogger('test')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def connect_sqlite(db_file):
    conn = sqlite3.connect(db_file)
    logger.info(f"Connected to SQLite database: {db_file}")
    return conn

def create_table(conn, table_name, columns: dict):
    cursor = conn.cursor()
    column_defs = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"
    logger.info(f"Creating table '{table_name}' with columns: {', '.join(columns.keys())}")
    cursor.execute(query)
    logger.info(f"Table '{table_name}' created or already exists")
    cursor.close()

def insert_dataframe(conn, df, table_name):
    cursor = conn.cursor()
    cols = ", ".join(df.columns)
    placeholders = ", ".join(["?"] * len(df.columns))
    insert_sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    values = [tuple(row) for row in df.values]
    cursor.executemany(insert_sql, values)
    conn.commit()
    logger.info(f"Inserted {len(df)} rows into table '{table_name}'")
    cursor.close()

def read_table(conn, table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    logger.info(f"Retrieved {len(df)} rows from table '{table_name}'")
    return df

def delete_table(conn, table_name):
    cursor = conn.cursor()
    query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(query)
    conn.commit()
    logger.info(f"Deleted table '{table_name}' if it existed")  
    cursor.close()

def main():
    db_file = "test_class.db"
    conn = connect_sqlite(db_file)
    table_name = "invoice"
    df = pd.read_csv("extracted_data.csv")
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]    
    columns = {col: "TEXT" for col in df.columns} 
    create_table(conn, table_name, columns)
    insert_dataframe(conn, df, table_name)
    retrieved_df = read_table(conn, table_name)
    logger.info(f"Data retrieved from table '{table_name}':\n{retrieved_df.head()}")
    # delete_table(conn, table_name)
    conn.close()

if _name_ == "_main_":
    main()




# Design a Python program using object-oriented programming that keeps track of pets in a clinic.

# Classes Required
# Pet class with:

# Attributes: name, age, species

# Method: display_info() → prints details in the format:
# " Name: Tommy | Age: 4 | Species: Dog"

# Clinic class with:

# Attribute: a list to store all pets

# Methods:

# add_pet(pet: Pet) – Adds a new pet object

# remove_pet(name: str) – Removes pet by name (case-insensitive)

# search_pet(name: str) – Searches and displays pet details

# display_all() – Displays all pet records

# if _name_ == "_main_":
#     main() 