import pandas as pd
import numpy as np
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

st.markdown("# Features")

st.markdown("### Exploration options")

st.markdown("There are no advanced exploration features available for `st.table`. Users can simply scroll through the table.")

st.markdown("### Editing options")

st.markdown("There are no editing options available for `st.table`. Users cannot sort, filter, or edit the data in any way.")

st.markdown("### Customization")

st.markdown("There is no customization available for `st.table`.")

st.markdown("### Performance")

st.markdown("`st.table` draws the entire table upon render, so it's not suitable for large datasets.")

with st.expander("Try using st.dataframe with different sized datasets"):
    num_rows = st.number_input("Number of Rows", value=10, key='num_rows')
    num_cols = st.number_input("Number of Columns", value=3, key='num_cols')

    st.code("""
    import pandas as pd
    import numpy as np

    # Create random data
    data = np.random.rand(num_rows, num_columns)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_columns)])

    st.table(df)
    """)

    # Define the number of rows and columns
    num_rows = num_rows
    num_columns = num_cols

    # Create random data
    data = np.random.rand(num_rows, num_columns)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_columns)])

    st.table(df)

