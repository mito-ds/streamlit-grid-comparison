
import pandas as pd
import streamlit as st

st.title("`st.dataframe`")

st.markdown("### When to use this grid")

st.markdown("""
- Your dataset is larger than what can be displayed with `st.table`
- You want to customize how the data is dispalyed in the grid
- Users need to sort the data, but not filter or edit the data
            
**TL;DR** - `st.dataframe` is great for letting users view a dataset, but not manipulate it.
""")

st.markdown("### Basic usage")

st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.dataframe(df)
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
st.dataframe(df)

st.markdown("### Customization")

st.markdown("There is a large amount of visual customization available for `st.dataframe`.")

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
        

st.markdown("### Exploration options")

st.markdown("`st.dataframe` supports filtering your dataset. This is the only exploration option available by default.")
st.markdown("If you want to add filtering to this grid, you can see a [Streamit Blog Post](https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/) explaing how to do so.")

st.markdown("### Editing options")

st.markdown("Althought you can sort, filter, and edit the data in a limited way, this is only for exploration purposes.")
st.markdown("You cannot save the edited data, or use it later in your streamlit application.")

st.markdown("### Performance")

st.markdown("`st.table` lays out the entire table at once, so it's not suitable for large datasets.")
