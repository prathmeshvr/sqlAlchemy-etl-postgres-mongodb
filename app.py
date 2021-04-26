from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData,Text,BigInteger,Integer,Float
import pandas as pd
import psycopg2

param_dic = {
    "host"      : "192.168.0.103",
    "database"  : "nyc",
    "user"      : "postgres",
    "password"  : "example"
}

connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" % (
    param_dic['user'],
    param_dic['password'],
    param_dic['host'],
    param_dic['database']
)

engine = create_engine(connect,echo=False)
## Data Extraction From Postgres SQL
df = pd.read_sql_table('nyc', engine)

# Now we will fill Missing Values