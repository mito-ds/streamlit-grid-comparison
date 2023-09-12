
import pandas as pd
import numpy as np
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

st.title("`Mito`")

st.markdown("### When to use this grid")

st.markdown("""
- Users want to edit their data like they do in Excel, including: sorting, filtering, Excel-like formulas, pivot tables, graphs, and more.
- You want to record the edits that users make to the spreadsheet, so you can reuse those edits on other datasets. Aka: you want to build an automation!
- You want the rest of your streamlit application to react to the data the user has selected
            
**TL;DR** - `Mito` is great for providing an Excel-like experience to your users. It also allows you to record the edits that users make, like recording a marco in Excel, but with Python.
""")

st.markdown("### Basic usage")

st.markdown('Since Mito is a third party library, you need to install it with `pip install mitosheet`.')

st.code("""
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
spreadsheet(df)
""")
        
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
spreadsheet(df)

st.markdown("# Features")

st.markdown("### Exploration options")

st.markdown("""
Mito provides a large number of exploration features, including:
1. [Graphing](https://docs.trymito.io/how-to/graphing). Try clicking the **Graph** button in the toolbar to generate a plotly graph. 
2. [Pivot tables](https://docs.trymito.io/how-to/pivot-tables). Try clicking the **Pivot** button in the toolbar.
3. [Sorting](https://docs.trymito.io/how-to/sort-data) and [filtering](https://docs.trymito.io/how-to/filter-data). Click the Filter icon inside any column header.
4. And much more. See our [documentation](https://docs.trymito.io) for more information.
            
All of these features work out of the box, with no additional code required.            
""")

st.markdown("### Editing options")

st.markdown("""
Mito aims to provide a full Excel-like editing experience, including:
1. [Excel-like Formulas](https://docs.trymito.io/how-to/interacting-with-your-data). Try typing `=SUM(` into any cell.
2. [Import from Excel, CSV, and Snowflake](https://docs.trymito.io/how-to/importing-data-to-mito). Try clicking the **Import** button in the toolbar.
3. [Renaming and removing column](https://docs.trymito.io/how-to/splitting-text-into-columns). Try clicking on a column then pressing **Delete** on your keyboard.
4. [AI transformations](https://docs.trymito.io/how-to/mito-ai). Try clicking on the **AI** button in the toolbar and sending a prompt.
5. And much more. See our [documentation](https://docs.trymito.io) for more information.

""")

st.subheader("Saving user edits")

st.markdown("### Customization")

st.markdown("""
Mito exposes frontend customization to the application user, including:
1. [Excel-style number formats](https://docs.trymito.io/how-to/formatting/column-formatting). Try selecting a number column and changing it to accounting mode.
2. [Excel-style conditional formatting](https://docs.trymito.io/how-to/formatting/conditional-formatting). Try selecting a column and clicking **Format > Conditional Formatting** button in the toolbar.                        

Mito Enterprise users have additional customization options, including:
1. [Custom importers](https://docs.trymito.io/how-to/customizing-the-toolbar)
2. [Custom spreadsheet functions](https://docs.trymito.io/how-to/interacting-with-your-data/bring-your-own-spreadsheet-functions)
""")

st.markdown("### Performance")

st.markdown("`Mito` is designed to work with any sized dataset. If you have a millions rows and tens of columns, it should work fine. As long as you can get it into a dataframe, you can use it in Mito.")

st.markdown("To support large datasets, Mito only renders the first 1500 rows and 1500 columns of each dataset. To see other parts of your dataset, apply a filter!")

with st.expander("Try using `Mito` with different sized datasets"):
    num_rows = st.number_input("Number of Rows", value=50000, key='num_rows')
    num_cols = st.number_input("Number of Columns", value=10, key='num_cols')

    st.code("""
    import pandas as pd
    import numpy as np

    # Create random data
    data = np.random.rand(num_rows, num_columns)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_columns)])

    spreasheet(df)
    """)

    # Create random data
    data = np.random.rand(num_rows, num_cols)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    spreadsheet(df)



# TODO:

# Third party library
# Limited visual customization
# Limited JS extensibililty (no custom JS callbacks) compared to AgGrid
