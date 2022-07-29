# Database extract pipeline
import sys, psycopg2 as sql
from sqlalchemy import create_engine
sys.path.append('..')

from ...secrets.getPW import getPW

def db_pipeline(db = 'ATP_tour_data', user = 'postgres', pw = getPW('ATP').strip(), query = '''SELECT * FROM "ATP_players";'''):
    # Set up engine
    engine = create_engine(f'postgresql+psycopg2://postgres:{pw}@localhost:5432/ATP_tour_data')
    
    # Set up connection
    conn = sql.connect(dbname = db, user = user, password = f'{pw}')
    cur = conn.cursor()

    # Execute & fetch data
    cur.execute(query)
    output = cur.fetchall()
    
    # Close connection & return output
    conn.close()
    return output

if __name__ == '__main__':
    import pandas as pd
    out = pd.DataFrame(db_pipeline(), columns=['Tournament', 'Rounds', 'Hours', 'Times_Entered', 'Matches', 'Wins', 'Win_pct', 'Avg_sets'])