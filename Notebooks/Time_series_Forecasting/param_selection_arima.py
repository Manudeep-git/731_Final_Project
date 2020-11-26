import pandas as pd
import numpy as np
import warnings
import itertools as it
from IPython.display import display
import statsmodels.api as sm
data = pd.read_csv(r'C:\Stuff\KU Study\EECS 731 Intro to Data Science\Final Semester Project\731_Final_Project\Contries_Data\Russia_history_data.csv')
data = data.drop(["Wind Chill", "Heat Index", "Snow Depth", "Wind Gust"],axis='columns')
data.dropna(subset = ["Visibility"], inplace=True)
data.dropna(subset = ["Cloud Cover"], inplace=True)
data.rename(columns={'Date time': 'Date', 'Maximum Temperature': 'Maximum_Temperature','Minimum Temperature': 'Minimum_Temperature','Wind Speed': 'Wind_Speed','Cloud Cover': 'Cloud_Cover','Relative Humidity': 'Relative_Humidity'}, inplace=True)
Date=data.Date.str.split("/",expand=True) 
Date['Combined'] = Date[2].str.cat(Date[0],sep="-")
Date['Combined'] = Date['Combined'].astype(str)+"-01"
data['Date'] =  Date['Combined']
data['Date']=data['Date'].astype('datetime64[ns]')
df=data[["Date","Temperature"]]
df = data.groupby(['Date'])['Temperature'].mean().reset_index()
df=df.set_index('Date')
p = d = q = range(0, 2)
pdq = list(it.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(it.product(p, d, q))]
warnings.simplefilter('always', category=UserWarning)
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(np.asarray(df), order=param, seasonal_order=param_seasonal, enforce_stationarity=False, enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue