import pandas as pd

dz={
    "name":[],
    "roll no":[],
    "sub 1":[],
    "sub 2":[],
    "sub 3":[],
    "sub 4":[],
    "sub 5":[],
    "percentage":[],
    "status":[]
}

df=pd.DataFrame(dz)
print(df)

df.to_csv("student result.csv",index=False)