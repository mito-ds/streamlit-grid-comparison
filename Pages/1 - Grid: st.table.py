import pandas as pd
import streamlit as st

st.title("`st.table`")

st.header("When to use this grid")

st.markdown("""
- The dataset being displayed is smaller - less than 50 rows
- You need to display the data without any visual customization
- Users do not need to be able to sort, filter, or edit the data in any way
            
**TL;DR** - `st.table` is great for displaying tiny datasets in a static table.
""")

st.header("Basic usage")

st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.table(df)
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.table(df)

st.header("Exploration options")

st.text("There are no editing options available for `st.table`. You simply can just scroll through the table.")

st.header("Editing options")

st.text("There are no editing options available for `st.table`.")
st.text('You cannot sort, filter, or edit the data in any way.')

st.header("Customization")

st.text("There is no customization available for `st.table`.")

st.header("Performance")

st.text("`st.table` lays out the entire table at once, so it's not suitable for large datasets.")

st.header("Pros and cons")

st.subheader("Pros")

st.markdown("""
- Easy to use
- Built-in
""")
            
st.subheader("Cons")

st.markdown("""
- No customization
- No editing options
- Not suitable for large datasets
""")
            
