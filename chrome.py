import io
import pandas as pd
import numpy as np
from IPython.display import display
from http import cookiejar

# Parse chrome Application -> Cookies into a dataframe.
#   Note: You must preserve or update the header, as-needed.
#         The header does not get copied.
df = pd.read_csv(io.FileIO('./chrome.txt'), sep='\t', header=0, index_col=False)

# Fill in NaNs and format True/False for cookies.txt.
df = df.fillna(False).assign(flag=True).replace({True: 'TRUE', False: 'FALSE'})

# Get unix timestamp from max_age
max_age = (
    df.max_age
    .replace({'Session': np.nan})
    .pipe(pd.to_datetime))
start = pd.Timestamp("1970-01-01", tz='UTC')
max_age = (
    ((max_age - start) // pd.Timedelta('1s'))
    .fillna(0)  # Session expiry are 0s
    .astype(int))  # Floats end with ".0"
df = df.assign(max_age=max_age)

display(df.to_string())

cookie_file_cols = ['domain', 'flag', 'path', 'secure', 'max_age', 'name', 'value']
with open('cookies.txt', 'w', encoding='utf-8') as fh:
  # Python's cookiejar wants this header.
  fh.write('# Netscape HTTP Cookie File\n')
  df[cookie_file_cols].to_csv(fh, sep='\t', index=False, header=False)

# Load and Save using cookiejar so we can normalize the output
moz = cookiejar.MozillaCookieJar()
moz.load('cookies.txt')
moz.save('moz.txt')
