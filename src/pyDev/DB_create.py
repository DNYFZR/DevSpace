import io, psycopg2 as sql, pandas as pd
from sqlalchemy import create_engine
from getPW import getPW

# Access token
db = 'ATP_tour_data'
table = 'matches'
user = 'postgres'
pw = getPW('ATP')

# Engine
engine = create_engine(f'postgresql+psycopg2://postgres:{pw}@localhost:5432/ATP_tour_data')

# Set up connection

conn = sql.connect(dbname = db, user = user, password = f'{pw}')
conn.autocommit = True
cur = conn.cursor()

# Create schema
cur.execute(
    '''
        CREATE SCHEMA IF NOT EXISTS ATP_tour_data;
    '''
)


# Bring in data from maintained csv
df = pd.read_csv(r'data/atp_matches_db.csv', index_col=0)

# build type mapping
type_dict = {
    "object": 'text'.upper(),
    "int64": 'int'.upper(),
    "float64": 'numeric'.upper(),
}

db_dict = df.dtypes.apply(lambda x: x.name).to_dict()

# Construct table creation query string
query_str = ''
n = 0
for col, col_type in db_dict.items():
    col_type = type_dict[col_type]
    if n == 0:
        sub_str = f'({col} {col_type}, '
    
    elif n == len(df.columns) - 1:
        sub_str = f'{col} {col_type})'

    else:
        sub_str = f'{col} {col_type}, '
    
    n += 1
    query_str += sub_str

# Create table with empty cols
query = f'CREATE TABLE IF NOT EXISTS {db}.{table}{query_str};'
cur.execute(query)

# Close psycopg2 connection 
conn.close()

# # Add data to table 
df.head(0).to_sql('matches', engine, if_exists='replace',index=False) #drops old table and creates new empty table

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'matches', null="") # null values become ''
conn.commit()

# check db
# cur.execute('SELECT * FROM matches LIMIT 5;')
# print(cur.fetchall())

# Close connection to DB
conn.close()