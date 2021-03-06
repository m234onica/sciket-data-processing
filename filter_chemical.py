import os
import glob
import pandas as pd


csv_file = os.path.join('./dataset', "*.csv")
data = pd.concat(map(pd.read_csv, glob.glob(csv_file)))

Result = os.path.join("./result", "filter_chemical.csv")
result = pd.DataFrame()

filter_id = ["181", "183", "184", "185", "199", "200", "210"]
for id in filter_id:
    output = data[data['行業代號（財政資訊中心匯入）'].str.match(id) |
                  data['行業代號（財政資訊中心匯入）'].str.contains("," + id)]
    result = result.append(output)

uni_result = result.drop_duplicates(subset=["公司名稱"], keep="first")
uni_result.to_csv(Result, index=False)
print("success: ", pd.read_csv(Result).shape)
