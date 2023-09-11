
import pandas as pd
import streamlit as st

st.title("`st.data_editor`")

st.header("When to use this grid")

st.markdown("""
- The dataset is larger than what can be displayed with `st.table`
- You want some visual customization of the data being displayed
- Users need to perform very basic data cleaning operations, such as:
    - Adding and removing rows
    - Editing specific values in the dataframe
            
**TL;DR** - `st.data_editor` is great for letting users view a dataset and perform very basic data cleaning operations on it.
""")

st.header("Basic usage")

st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
new_df = st.data_editor(df)

st.write('You edited', (df != new_df).sum().sum(), 'values')
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
new_df = st.data_editor(df)

st.write('You edited', (df != new_df).sum().sum(), 'values')

st.header("Exploration options")

# TODO

st.header("Editing options")

# TODO:

st.header("Customization")

st.text("Similar to `st.dataframe`, there are a large amount of customization options available for `st.data_editor`.")

st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
new_df = st.data_editor(
    df,
    column_config={
        "airline": "Airline",
        "avail_seat_km_per_week": st.column_config.NumberColumn(
            "Available Seat Km per Week",
            format="%d km ✈️",
            min_value=0
        ),
    },
    num_rows="dynamic",
    disabled=["fatal_accidents_00_14", "fatalities_00_14"],
    hide_index=True,
)

st.write('You edited', (df != new_df).sum().sum(), 'values')
""")
        
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
new_df = st.data_editor(
    df,
    column_config={
        "airline": "Airline",
        "avail_seat_km_per_week": st.column_config.NumberColumn(
            "Available Seat Km per Week",
            format="%d km ✈️",
            min_value=0
        ),
    },
    num_rows="dynamic",
    disabled=["fatal_accidents_00_14", "fatalities_00_14"],
    hide_index=True,
)
st.write('You edited', (df != new_df).sum().sum(), 'values')

        

st.header("Performance")

# TODO:

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