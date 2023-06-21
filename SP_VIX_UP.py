# -*- coding: utf-8 -*-
"""
Analisis de la frecuencia de sesiones de movimientos simultaneos en el S&P y el VIX
Los dos suben o los dos bajan de cierre a cierre diario
"""
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor 
import mplfinance as mpf


start = '2016-01-01'
end = datetime.today().strftime('%Y-%m-%d')

df =  yf.download(['^GSPC', '^VIX'], start=start, end=end)['Close']
df.columns = ['SP500', 'VIX']

df['PCT_SP500'] = df['SP500'].pct_change() * 100
df['PCT_VIX'] = df['VIX'].pct_change() * 100


## Los dos suben
spfiltro0 = 0.0
vixfiltro0 = 0.0
spfiltro1 = 0.3
vixfiltro1 = 1.0
spfiltro2 = 0.3
vixfiltro2 = 3.0
spfiltro3 = 0.5
vixfiltro3 = 1.0
spfiltro4 = 0.8
vixfiltro4 = 5.0

filter0 = (df['PCT_SP500'] > spfiltro0) & (df['PCT_VIX'] > vixfiltro0)
filter1 = (df['PCT_SP500'] > spfiltro1) & (df['PCT_VIX'] > vixfiltro1)
filter2 = (df['PCT_SP500'] > spfiltro2) & (df['PCT_VIX'] > vixfiltro2)
filter3 = (df['PCT_SP500'] > spfiltro3) & (df['PCT_VIX'] > vixfiltro3)
filter4 = (df['PCT_SP500'] > spfiltro4) & (df['PCT_VIX'] > vixfiltro4)

df['Suben_0'] = None
df.loc[filter0, 'Suben_0'] = 0
df['Suben_1'] = None
df.loc[filter1, 'Suben_1'] = 1
df['Suben_2'] = None
df.loc[filter2, 'Suben_2'] = 2
df['Suben_3'] = None
df.loc[filter3, 'Suben_3'] = 3
df['Suben_4'] = None
df.loc[filter4, 'Suben_4'] = 4


## Los dos bajan
spfiltro0 = spfiltro0 * -1
vixfiltro0 = vixfiltro0 * -1
spfiltro1 = spfiltro1 * -1
vixfiltro1 = vixfiltro1 * -1
spfiltro2 = spfiltro2 * -1
vixfiltro2 = vixfiltro2 * -1
spfiltro3 = spfiltro3 * -1
vixfiltro3 = vixfiltro3 * -1
spfiltro4 = spfiltro4 * -1
vixfiltro4 = vixfiltro4 * -1

filter0 = (df['PCT_SP500'] < spfiltro0) & (df['PCT_VIX'] < vixfiltro0)
filter1 = (df['PCT_SP500'] < spfiltro1) & (df['PCT_VIX'] < vixfiltro1)
filter2 = (df['PCT_SP500'] < spfiltro2) & (df['PCT_VIX'] < vixfiltro2)
filter3 = (df['PCT_SP500'] < spfiltro3) & (df['PCT_VIX'] < vixfiltro3)
filter4 = (df['PCT_SP500'] < spfiltro4) & (df['PCT_VIX'] < vixfiltro4)

df['Bajan_0'] = None
df.loc[filter0, 'Bajan_0'] = 0
df['Bajan_1'] = None
df.loc[filter1, 'Bajan_1'] = 1
df['Bajan_2'] = None
df.loc[filter2, 'Bajan_2'] = 2
df['Bajan_3'] = None
df.loc[filter3, 'Bajan_3'] = 3
df['Bajan_4'] = None
df.loc[filter4, 'Bajan_4'] = 4


# GRAFICO
fig, axs = plt.subplots(4, 1, figsize=(12, 12), sharex=True,  gridspec_kw={'height_ratios': [3, 3, 2, 2], 'hspace': 0.3})

axs[0].plot(df.index, df['SP500'], color ='purple')
axs[0].set_ylabel('SP500')

axs[1].plot(df.index, df['VIX'], color='blue')
axs[1].set_ylabel('VIX')

axs[2].scatter(df.index, df['Suben_0'], marker= '^', s= 15, color ='grey')
axs[2].scatter(df.index, df['Suben_1'], marker= '^', s= 15, color ='green')
axs[2].scatter(df.index, df['Suben_2'], marker= '^', s= 15, color ='yellow')
axs[2].scatter(df.index, df['Suben_3'], marker= '^', s= 15, color ='orange')
axs[2].scatter(df.index, df['Suben_4'], marker= '^', s= 15, color ='red')
axs[2].set_title('Ambos suben')

axs[2].set_yticks([0, 1, 2, 3, 4])
axs[2].set_yticklabels([f'SP > {-spfiltro0}% & VIX > {-vixfiltro0}%', f'SP > {-spfiltro1}% & VIX > {-vixfiltro1}%',
                        f'SP > {-spfiltro2}% & VIX > {-vixfiltro2}%', f'SP > {-spfiltro3}% & VIX > {-vixfiltro3}%',
                        f'SP > {-spfiltro4}% & VIX > {-vixfiltro4}%'], fontsize= 8)

axs[3].scatter(df.index, df['Bajan_0'], marker= 'v', s= 15, color ='grey')
axs[3].scatter(df.index, df['Bajan_1'], marker= 'v', s= 15, color ='green')
axs[3].scatter(df.index, df['Bajan_2'], marker= 'v', s= 15, color ='yellow')
axs[3].scatter(df.index, df['Bajan_3'], marker= 'v', s= 15, color ='orange')
axs[3].scatter(df.index, df['Bajan_4'], marker= 'v', s= 15, color ='red')
axs[3].set_title('Ambos bajan')

axs[3].set_yticks([0, 1, 2, 3, 4])
axs[3].set_yticklabels([f'SP < {-spfiltro0}% & VIX < {-vixfiltro0}%', f'SP < {spfiltro1}% & VIX < {vixfiltro1}%',
                        f'SP < {spfiltro2}% & VIX < {vixfiltro2}%', f'SP < {spfiltro3}% & VIX < {vixfiltro3}%',
                        f'SP < {spfiltro4}% & VIX < {vixfiltro4}%'], fontsize= 8)

plt.xlabel('Date')
plt.suptitle('DÍAS CON MOVIMIENTO S&P500 Y VIX EN EL MISMO SENTIDO')

multi = MultiCursor(None, (axs[0], axs[1], axs[2], axs[3]), color='r', lw=1)
plt.show()





