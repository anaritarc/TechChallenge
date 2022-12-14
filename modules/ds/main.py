#Pseudocode

from feature_selection import feature_selection  
from model import model
import pickle

# Loading the dataset and visualizing summary statistics
username = 'admin'
password = 'admin' 
host_name = 'hostname'
port = 5432
db_name = 'operation-db'
schema = 'companydata'

conn_str = 'postgresql://{}:{}@{}:{}/{}'.format(username, password, host_name, port, db_name)
conn_args = {'options': '-csearch_path={}'.format(schema)}

with open('queries/table1.sql') as query_from_file:
    df = pd.read_sql_query(query_from_file.read(), engine)
    
    
## Feature selection
df_train = feature_selection(df)
## Model train 
model (df_train)

with open('pred_mod.pkl', 'wb') as model_file:
  pickle.dump(model, model_file)