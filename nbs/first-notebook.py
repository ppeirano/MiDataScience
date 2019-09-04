import seaborn as sns
import sys
sys.path.append("../src")
import utils

print("Comenzando.....")
df = sns.load_dataset("titanic")
print(df.head(1))

utils.hello_world()

utils.show_df(df)