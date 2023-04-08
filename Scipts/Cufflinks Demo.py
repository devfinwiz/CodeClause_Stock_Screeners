'''Demo usage of cufflinks. Currently incomplete'''

import numpy as np
import pandas as pd
import yfinance as yf
import warnings

import cufflinks as cf
import plotly.graph_objects as go
import matplotlib.pyplot as plt


cf.set_config_file(theme='pearl',sharing='public',offline=True)
apple_df = pd.read_csv(r'Auto generated Dataset\ABFRL.NS.csv', index_col=0, parse_dates=True)

qf=cf.QuantFig(apple_df,title='ABFRL Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
qf.add_volume()

qf.iplot()