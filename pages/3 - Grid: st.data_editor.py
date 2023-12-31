
import pandas as pd
import numpy as np
import streamlit as st

st.title("`st.data_editor`")

st.markdown("### When to use this grid")

st.markdown("""
- Your dataset is larger than what should be displayed with `st.table` -- more than 30 rows and 5 columns
- You want to customize how the data is dispalyed in the grid
- Users need to perform basic data cleaning operations, such as:
    - Adding and removing rows
    - Editing specific values in the dataframe
            
**TL;DR** - `st.data_editor` is great for letting users view a dataset and perform basic data cleaning operations on it.
""")

st.markdown("### Basic usage")

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


st.markdown("# Features")

st.markdown("### Exploration options")

st.markdown("`st.data_editor` supports the same exploration options as `st.dataframe`: sorting, column resizing, and table search are supported out of the box. These are the only exploration options available by default.")
st.markdown("However, if you want to add filtering to `st.data_editor`, you can follow this [Streamit Blog Post](https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/) which uses Streamlit inputs and multiselects to filter the dataframe before rendering it in the grid.")

st.markdown("### Editing options")

st.markdown("""`st.data_editor` supports: 
- Editing specific cells - simply double click on a cell to edit it
- Deleting rows - select a row and then press `Delete`
- Adding rows - click on the bottom row and enter data""")

with st.expander("Editing options for `st.data_editor`"):
    st.code("""
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
edited_df = st.data_editor(df, num_rows="dynamic")

st.write(edited_df)
""")
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    edited_df = st.data_editor(df, num_rows="dynamic")



    st.write(edited_df)

st.markdown("### Customization")

st.markdown("Similar to `st.dataframe`, there are a large amount of customization options available for `st.data_editor`.")

with st.expander("Using column-level and dataframe-wide configurations"):
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

with st.expander("Using Pandas stylers"):
    st.code("""
        import streamlit as st
        import pandas as pd
                
        df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
        st.data_editor(
            df.style.highlight_max(axis=0),
            hide_index=True,
        )
    """)

    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    st.data_editor(
        df,
        hide_index=True,
    )

        
st.markdown("### Performance")

st.markdown("`st.data_editor` is designed to work for medium-sized data sets. If you have a few million rows and ~10 columns, it should work fine.")

st.markdown("By default, if your data is more than 200.0 MB, it won't render in st.data_editor.")

with st.expander("Try using st.data_grid with different sized datasets"):
    num_rows = st.number_input("Number of Rows", value=50000, key='num_rows')
    num_cols = st.number_input("Number of Columns", value=10, key='num_cols')

    st.code("""
    import pandas as pd
    import numpy as np

    # Create random data
    data = np.random.rand(num_rows, num_cols)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    st.data_editor(
        df,
        hide_index=True,
        key='data_editor_performance_test'
    )
    """)

    # Create random data
    data = np.random.rand(num_rows, num_cols)

    # Convert the NumPy array to a DataFrame
    data = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    st.data_editor(
        df,
        hide_index=True,
        key='data_editor_performance_test'
    )
