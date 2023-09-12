
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import numpy as np

st.title("`AgGrid`")

st.markdown("### When to use this grid")

st.markdown("""
- You want advanced visual customization of the data being displayed
- You want users to be able to sort, filter, and perform basic editing operations on the data
- You want the rest of your streamlit application to react to the data the user has selected
            
**TL;DR** - `AgGrid` offers slightly exploration and editing options than `st.dataframe`, and allows for the most visual customization of any grid.
""")

st.markdown("### Basic usage")

st.markdown('As AgGrid is a third party library, you need to install it with `pip install streamlit-aggrid`.')

st.code("""
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
        
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df, height=250)
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df, height=300)


st.markdown("# Features")

st.markdown("### Exploration options")

st.markdown("""
By default, AgGrid provides a few exploration features, including:
1. Sorting data - click on the column header to sort the data
2. Filtering data - click on the column header dropdown to filter the data
3. Hiding or pining columns for better visibility

Beyond the default, AgGrid provides a large number of configurable exploration features, including:
1. Highlighting cells based on their value
""")

st.markdown("### Editing options")

st.markdown("""
AgGrid provides three basic editing options:
1. Sorting data - click on the column header to sort the data
2. Filtering data - click on the column header dropdown to filter the data
3. Editing specific cells - simply double click on a cell to edit it
""")
            
with st.expander("Getting sorted, filtered, and edited data back from `AgGrid`"):
    st.code("""
import streamlit as st
import pandas as pd 
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode
            
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
                
grid_response = AgGrid(
    df, 
    height=300, 
    width='100%',
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED, 
    editable=True
)

df = grid_response['data']
st.write(df)
""")
                
    from st_aggrid import AgGrid, DataReturnMode

    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
                
    grid_response = AgGrid(
        df, 
        height=300, 
        width='100%',
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED, 
        editable=True
    )

    df = grid_response['data']
    st.write(df)


st.markdown("### Customization")

st.markdown("""
AgGrid provides a huge variety of visual customization options, including:
1. Specifying the grid size with the `height` and `width` parameters
2. Custom JavaScript snippets to render cells in the grid.
3. Creating virtual columns that are not present in the original dataset
4. Theming
5. Pre-selecting rows
            
You can see more examples of AgGrid customization in the [AgGrid documentation](https://staggrid-examples.streamlit.app).
""")
            
with st.expander("Using custom JavaScript snippets to render cells in the grid"):
    st.code("""
import numpy as np
import pandas as pd
import streamlit as st
            
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode,GridUpdateMode

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

# an example based on https://www.ag-grid.com/javascript-data-grid/component-cell-renderer/#simple-cell-renderer-example
BtnCellRenderer = JsCode('''
class BtnCellRenderer {
    init(params) {
        this.params = params;
        this.eGui = document.createElement('div');
        this.eGui.innerHTML = `
         <span>
            <button id='click-button' 
                class='btn-simple' 
                style='color: ${this.params.color}; background-color: ${this.params.background_color}'>Click!</button>
         </span>
      `;

        this.eButton = this.eGui.querySelector('#click-button');

        this.btnClickedHandler = this.btnClickedHandler.bind(this);
        this.eButton.addEventListener('click', this.btnClickedHandler);

    }

    getGui() {
        return this.eGui;
    }

    refresh() {
        return true;
    }

    destroy() {
        if (this.eButton) {
            this.eGui.removeEventListener('click', this.btnClickedHandler);
        }
    }

    btnClickedHandler(event) {
        if (confirm('Are you sure you want to CLICK?') == true) {
            if(this.params.getValue() == 'clicked') {
                this.refreshTable('');
            } else {
                this.refreshTable('clicked');
            }
                console.log(this.params);
                console.log(this.params.getValue());
            }
        }

    refreshTable(value) {
        this.params.setValue(value);
    }
};
''')

df = make_data()
gb = GridOptionsBuilder.from_dataframe(df)

gb.configure_default_column(editable=True)
grid_options = gb.build()

grid_options['columnDefs'].append({
    "field": "clicked",
    "header": "Clicked",
    "cellRenderer": BtnCellRenderer,
    "cellRendererParams": {
        "color": "red",
        "background_color": "black",
    },
})


response = AgGrid(
    df,
    theme="streamlit",
    height=300,
    gridOptions=grid_options,
    allow_unsafe_jscode=True,
    fit_columns_on_grid_load=True,
    reload_data=False,
    try_to_convert_back_to_original_types=False
)

st.write(response['data'])
try:
    st.write(response['data'][response['data'].clicked == 'clicked'])
except:
    st.write('Nothing was clicked')
""")

    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

    # an example based on https://www.ag-grid.com/javascript-data-grid/component-cell-renderer/#simple-cell-renderer-example
    BtnCellRenderer = JsCode('''
    class BtnCellRenderer {
        init(params) {
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = `
            <span>
                <button id='click-button' 
                    class='btn-simple' 
                    style='color: ${this.params.color}; background-color: ${this.params.background_color}'>Click!</button>
            </span>
        `;

            this.eButton = this.eGui.querySelector('#click-button');

            this.btnClickedHandler = this.btnClickedHandler.bind(this);
            this.eButton.addEventListener('click', this.btnClickedHandler);

        }

        getGui() {
            return this.eGui;
        }

        refresh() {
            return true;
        }

        destroy() {
            if (this.eButton) {
                this.eGui.removeEventListener('click', this.btnClickedHandler);
            }
        }

        btnClickedHandler(event) {
            if (confirm('Are you sure you want to CLICK?') == true) {
                if(this.params.getValue() == 'clicked') {
                    this.refreshTable('');
                } else {
                    this.refreshTable('clicked');
                }
                    console.log(this.params);
                    console.log(this.params.getValue());
                }
            }

        refreshTable(value) {
            this.params.setValue(value);
        }
    };
    ''')

    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_default_column(editable=True)
    grid_options = gb.build()

    grid_options['columnDefs'].append({
        "field": "clicked",
        "header": "Clicked",
        "cellRenderer": BtnCellRenderer,
        "cellRendererParams": {
            "color": "red",
            "background_color": "black",
        },
    })


    response = AgGrid(
        df,
        theme="streamlit",
        height=300,
        gridOptions=grid_options,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=True,
        reload_data=False,
        try_to_convert_back_to_original_types=False
    )

with st.expander("Creating virtual columns that are not present in the original dataset"):
    st.code("""
import streamlit as st
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilde
            
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

gb = GridOptionsBuilder.from_dataframe(df)

gb.configure_columns(list(df.columns), editable=True)

#Create a calculated column that updates when data is edited. Use agAnimateShowChangeCellRenderer to show changes   
gb.configure_column('virtual column total incidents', valueGetter='Number(data.incidents_85_99) + Number(data.incidents_00_14)', cellRenderer='agAnimateShowChangeCellRenderer', editable='false', type=['numericColumn'])
go = gb.build()

ag = AgGrid(
    data, 
    gridOptions=go, 
    height=300, 
    fit_columns_on_grid_load=True, 
    reload_data=reload_data
)
""")
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_columns(list(df.columns), editable=True)

    #Create a calculated column that updates when data is edited. Use agAnimateShowChangeCellRenderer to show changes   
    gb.configure_column('virtual column total incidents', valueGetter='Number(data.incidents_85_99) + Number(data.incidents_00_14)', cellRenderer='agAnimateShowChangeCellRenderer', editable='false', type=['numericColumn'])
    go = gb.build()

    ag = AgGrid(
        df, 
        gridOptions=go, 
        height=300, 
        fit_columns_on_grid_load=True, 
    )

with st.expander("Theming"):
    st.code("""
import streamlit as st
import pandas as pd
import numpy as np

from st_aggrid import AgGrid, GridOptionsBuilder

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

selected_theme = st.selectbox("Theme", ["streamlit", "alpine", "balham""material"])
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection('multiple', pre_selected_rows=[3,5])

response = AgGrid(
    df,
    editable=True,
    height=300,
    gridOptions=gb.build(),
    data_return_mode="filtered_and_sorted",
    theme=selected_theme
)     
""")
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

    selected_theme = st.selectbox("Theme", ["streamlit", "alpine", "balham", "material"])
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('multiple', pre_selected_rows=[3,5])

    response = AgGrid(
        df,
        editable=True,
        height=300,
        gridOptions=gb.build(),
        theme=selected_theme
    )    


st.markdown("### Performance")

st.markdown("Streamlit `AgGrid` is built on top of the JavaScript `AgGrid` library, and as such is designed to work with large JavaScript datasets. However, Similar to `st.dataframe` and `st.data_editor`, if your data is more than 200.0 MB, it won't render in `AgGrid` by default.")

st.markdown("When using `AgGrid`, make sure to set a height, else all rows will be rendered and potentially crash your browser tab.")

with st.expander("Try using `AgGrid` with different sized datasets"):
    num_rows = st.number_input("Number of Rows", value=5000, key='num_rows')
    num_cols = st.number_input("Number of Columns", value=10, key='num_cols')

    st.code("""
    import pandas as pd
    import numpy as np

    # Create random data
    data = np.random.rand(num_rows, num_columns)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_columns)])

    AgGrid(df, height=250)
    """)

    # Create random data
    data = np.random.rand(num_rows, num_cols)

    # Convert the NumPy array to a DataFrame
    df = pd.DataFrame(data, columns=[f'Column_{i}' for i in range(num_cols)])

    AgGrid(df, height=250)
