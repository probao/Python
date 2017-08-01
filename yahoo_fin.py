#ImportError: The pandas.io.data module is moved to a separate package (pandas-datareader). 
#After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), 
#you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 27)
f = web.DataReader("F", 'yahoo', start, end)


