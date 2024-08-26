from pathlib import Path 
import pandas as pd 

current_path = Path(__file__).parent
data_path = current_path / "data"

print("\n"*5)
print(data_path)

print("\n"*5)

# operator overloadat __div__() metoden

df = pd.read_csv(data_path / "kladd.csv")

print(df)