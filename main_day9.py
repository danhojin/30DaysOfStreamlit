import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt
from vega_datasets import data

source = data.stocks()

st.header('Day 9: Line chart')

st.write('Get sample in a tidy dataframe format')

source_wide = source.pivot(index='date', columns='symbol', values='price')
source_wide.index.name = None
source_wide.columns.name = None

st.write('''
```python
from vega_datasets import data

source = data.stocks()
```
''')

st.write(source.head(), 'and now you have a wide dataframe')

st.write('''
```python
source_wide = source.pivot(index='date', columns='symbol', values='price')
source_wide.index.name = None
source_wide.columns.name = None
```

Note that you need to reset index and column names in order for **st.line_chart** to work properly.
''')

st.write(source_wide.head(), 'Now you get a line chart with **st.line_chart**')

# st.line_chart(source_wide.reset_index(drop=True)[['AAPL']])

st.line_chart(source_wide)

st.write('Alternatively, you can use a long dataframe which I prefer to a wide dataframe with **st.altair_char**')

st.markdown("""
```python
c = alt.Chart(source).mark_line().encode(
    x='date',
    y='price',
    color='symbol',
)

st.altair_chart(c)
```
""")

c = alt.Chart(source).mark_line().encode(
    x='date',
    y='price',
    color='symbol',
)

st.altair_chart(c)

st.write('Or, you can use **st.plotly_chart**')

st.markdown("""
```python
fig = px.line(source_wide, x=source_wide.index, y=source_wide.columns)
st.plotly_chart(fig)
```
""")


fig = px.line(source_wide, x=source_wide.index, y=source_wide.columns)
st.plotly_chart(fig)