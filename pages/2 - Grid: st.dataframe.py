
import pandas as pd
import numpy as np
import streamlit as st

st.title("`st.dataframe`")

st.markdown("### When to use this grid")

st.markdown("""
- Your dataset is larger than what should be displayed with `st.table` -- more than 30 rows and 5 columns
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
   
st.markdown("# Features")

st.markdown("### Exploration options")

st.markdown("`st.dataframe` supports sorting, column resizing, and table search out of the box. These are the only exploration options available by default.")
st.markdown("However, if you want to add filtering to `st.dataframe`, you can follow this [Streamit Blog Post](https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/) which uses Streamlit inputs and multiselects to filter the dataframe before rendering it in the grid.")

st.markdown("### Editing options")

st.markdown("Althought you can sort and edit the data in a limited way, this is only for exploration purposes.")
st.markdown("You cannot save the edited data, or use it later in your streamlit application.")

st.markdown("### Customization")

st.markdown("There is a large amount of visual customization available for `st.dataframe`.")

with st.expander("Using column-level configurations"):
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

with st.expander("Using Pandas stylers"):
    st.code("""
    import streamlit as st
    import pandas as pd
            
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    st.dataframe(
        df.style.highlight_max(axis=0),
        hide_index=True,
    )
    """)
            
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    st.dataframe(
        df.style.highlight_max(axis=0),
        hide_index=True,
    )
     

st.markdown("### Performance")

st.markdown("`st.dataframe` is designed to work for medium-sized data sets. If you have a few million rows and ~10 columns, it should work fine.")

st.markdown("By default, if your data is more than 200.0 MB, it won't render in st.dataframe.")

with st.expander("Try using st.dataframe with different sized datasets"):
    num_rows = st.number_input("Number of Rows", value=50000, key='num_rows')
    num_cols = st.number_input("Number of Columns", value=10, key='num_cols')

    st.code("""
    import pandas as pd
    import numpy as np

    # Create random data
    data = np.random.rand(num_rows, num_cols)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    st.dataframe(
        df,
        hide_index=True,
    )
    """)

    # Create random data
    data = np.random.rand(num_rows, num_cols)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    st.dataframe(
        df,
        hide_index=True,
    )
