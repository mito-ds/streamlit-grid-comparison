import pandas as pd
import streamlit as st

st.title("`st.table`")

st.markdown("### When to use this grid")

st.markdown("""
- Your dataset is small: less than 30 rows and 5 columns
- You don't need any custom data visualizations -- just a plain table
- Users don't need to sort, filter, or edit the data in any way
            
**TL;DR** - `st.table` is great for displaying tiny datasets in a static table.
""")

st.markdown("### Basic usage")

st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.table(df)
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.table(df)

st.markdown("### Exploration options")

st.markdown("There are no editing options available for `st.table`. You simply can just scroll through the table.")

st.markdown("### Editing options")

st.markdown("There are no editing options available for `st.table`.")
st.markdown('You cannot sort, filter, or edit the data in any way.')

st.markdown("### Customization")

st.markdown("There is no customization available for `st.table`.")

st.markdown("### Performance")

st.markdown("`st.table` lays out the entire table at once, so it's not suitable for large datasets.")
