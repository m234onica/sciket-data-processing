import os
import glob
import pandas as pd


csv_file = os.path.join('./result', "filter_chemical.csv")
data = pd.read_csv(csv_file)

output = pd.DataFrame(columns=["公司地址", "count"])

area = data["公司地址"].str.slice(0, 3)
output = data["公司名稱"].groupby(area).count()

print(output)

Result = os.path.join("./result", "Agg_chemical.csv")
output.to_csv(Result)
