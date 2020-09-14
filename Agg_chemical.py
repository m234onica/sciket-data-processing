import os
import glob
import pandas as pd


csv_file = os.path.join('./result', "filter_chemical.csv")
data = pd.read_csv(csv_file)

output = pd.DataFrame()
area = data["公司地址"].str.slice(0, 3)
output["Count"] = data.groupby(area)["公司名稱"].count()

print(output)

Result = os.path.join("./result", "Agg_chemical.csv")
output.to_csv(Result)
