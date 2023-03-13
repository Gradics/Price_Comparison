import pandas as pd
dfAuchan = pd.read_pickle("dfAuchan.pkl")
dfkifli = pd.read_pickle("dfkifli.pkl")
PriceMerge = pd.concat([dfAuchan, dfkifli], axis=1)
PriceMerge.to_pickle("PriceMerge.pkl")
# print(PriceMerge)