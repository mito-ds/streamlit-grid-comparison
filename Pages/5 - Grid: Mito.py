
import pandas as pd
import streamlit as st

st.title("`AgGrid`")

st.markdown("### When to use this grid")

st.markdown("""
- You want to provide users with a spreadsheet that they can edit like an Excel document, including sorting, filtering, formulas, pivot tables, and more.
- You want to automate the edits that users make to the spreadsheet, and reuse those edits on other datasets.
- You want the rest of your streamlit application to react to the data the user has selected
            
**TL;DR** - `Mito` is great for providing an Excel-like experience to your app users. It also allows you to automate the edits that users make to the spreadsheet, like recording a marco in Excel, but with Python.
""")

st.markdown("### Basic usage")

st.markdown('As AgGrid is a third party library, you need to install it with `pip install mitosheet`.')

st.code("""
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
spreadsheet(df)
""")
        
from mitosheet.streamlit.v1 import spreadsheet

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
spreadsheet(df)

st.markdown("### Exploration options")

st.markdown("""
Mito provides a large amount of exploration options, including:
1. [Graphing](https://docs.trymito.io/how-to/graphing). Try clicking the **Graph** button in the toolbar to generate a plotly graph. 
2. [Pivot tables](https://docs.trymito.io/how-to/pivot-tables). Try clicking the **Pivot** button in the toolbar.
3. [Sorting](https://docs.trymito.io/how-to/sort-data) and [filtering](https://docs.trymito.io/how-to/filter-data). Click the Filter icon inside any column header.
4. And much more. See our [documentation](https://docs.trymito.io) for more information.
            
All of these features are enabled out of the box, with no additional code required.            
""")

st.markdown("### Editing options")

st.markdown("""
Mito aims to provide a full Excel-like experience, including:
1. [Excel-like Formulas](https://docs.trymito.io/how-to/interacting-with-your-data). Try typing `=SUM(` into any cell.
2. [Import from Excel, CSV, and Snowflake](https://docs.trymito.io/how-to/importing-data-to-mito). Try clicking the **Import** button in the toolbar.
3. [Renaming and removing column](https://docs.trymito.io/how-to/splitting-text-into-columns). Try clicking the **Split** button in the toolbar.

""")

st.subheader("Saving user edits")

st.markdown("### Customization")

st.markdown("""
Mito exposes frontend customization to the application user, including:
1. [Excel-style formatting](https://docs.trymito.io/how-to/formatting)
2. TODO
                        
Mito Enterprise provides additional customization options, including:
1. [Custom importers](https://docs.trymito.io/how-to/customizing-the-toolbar)
2. [Customizing the sidebar](https://docs.trymito.io/how-to/customizing-the-sidebar)
3. [Customizing the context menu](https://docs.trymito.io/how-to/customizing-the-context-menu)
""")

st.markdown("### Performance")

# TODO:

# Third party library
# Limited visual customization
# Limited JS extensibililty (no custom JS callbacks) compared to AgGrid
