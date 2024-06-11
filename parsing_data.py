import pandas as pd

import numpy as np

datamin = pd.read_json('https://drive.google.com/uc?id=1Ha_yKTL6vAFmDdHGw8skAsq-aF4ohYhF')
datamin = pd.DataFrame(datamin)

timeseries = pd.read_json('https://drive.google.com/uc?id=1RF8GQFYDnICw2gmGQkKo5wZl43gC8ab3')
timeseries = pd.DataFrame(timeseries)
# print(datamin)
print(timeseries)
