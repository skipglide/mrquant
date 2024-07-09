import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

historical_data = yf.download("QQQ", start="2010-01-01", end="2023-01-01")
