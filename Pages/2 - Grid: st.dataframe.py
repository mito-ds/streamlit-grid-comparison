
import pandas as pd
import streamlit as st

st.title("`st.dataframe`")

st.header("When to use this grid")

st.markdown("""
- The dataset is larger than what can be displayed with `st.table`
- You want some visual customization of the data being displayed
- While users need to sort, they do not need to filter or edit the data
            
**TL;DR** - `st.dataframe` is great for letting users view a dataset, but not manipulate it.
""")

st.header("Basic usage")

st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.dataframe(df)
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.dataframe(df)

st.header("Customization")

st.text("There is a large amount of visual customization available for `st.dataframe`.")

st.code("""
import streamlit as st
import pandas as pd
        
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.dataframe(
    df,
    column_config={
        "airline": "Airline",
        "avail_seat_km_per_week": st.column_config.NumberColumn(
            "Available Seat Km per Week",
            format="%d km",
        ),
    },
    hide_index=True,
)
""")
        
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.dataframe(
    df,
    column_config={
        "airline": "Airline",
        "avail_seat_km_per_week": st.column_config.NumberColumn(
            "Available Seat Km per Week",
            format="%d km ✈️",
        ),
    },
    hide_index=True,
)
        

st.header("Exploration options")

st.text("`st.dataframe` supports filtering your dataset. This is the only exploration option available by default.")
st.text("If you want to add filtering to this grid, you can see a [Streamit Blog Post](https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/) explaing how to do so.")

st.header("Editing options")

st.text("Althought you can sort, filter, and edit the data in a limited way, this is only for exploration purposes.")
st.text("You cannot save the edited data, or use it later in your streamlit application.")

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