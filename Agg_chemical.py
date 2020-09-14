import os
import glob
import pandas as pd


csv_file = os.path.join('./result', "filter_chemical.csv")
data = pd.read_csv(csv_file)

output_address = pd.DataFrame()
address = data["公司地址"].str.slice(0, 3)
output_address["Count"] = data.groupby(address)["公司名稱"].count()

output_capital = pd.DataFrame()
bins = [x * 1000000 for x in range(100000)]
capital = pd.cut(data["實收資本額"], bins, right=False)

output_capital["Count"] = data["公司名稱"].groupby(capital).count()

Result = os.path.join("./result", "Agg_chemical.csv")
result = pd.concat([output_address, output_capital])

result.to_csv(Result)
