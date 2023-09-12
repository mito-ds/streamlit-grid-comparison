
import streamlit as st
# Questions
# My dataset has > 50 rows
# 


def get_grid_recconmendation(
    has_greater_than_50_rows,
    has_greater_than_1M_rows,
    want_built_in_sorting,
    want_built_in_filtering,
    want_built_in_excel_formulas,
    want_built_in_pivot_tables,
    want_edits_to_propogate_to_rest_of_app,
    want_automation
):

    if want_automation: 
        return "Mito"

    if want_built_in_excel_formulas:
        return "Mito"

    if has_greater_than_1M_rows: 
        return "Mito"

    if want_edits_to_propogate_to_rest_of_app: 
        return "Mito or AgGrid"

    if want_built_in_pivot_tables:
        return "Mito or AgGrid" # TODO: Figure out if this is supported out of the box

    if want_built_in_filtering:
        return "Mito or AgGrid"

    if want_built_in_sorting or want_built_in_single_cell_editing or has_greater_than_50_rows:
        return "st.data_editor or st.dataframe"

    return "st.table"
    

st.markdown('### The Grid Quiz: Which Grid is Right For Me?')

with st.form("grid_quiz"):
    st.write("Check the boxes that apply to you.")
    has_greater_than_50_rows = st.checkbox("My dataset has > 50 rows")
    has_greater_than_1M_rows = st.checkbox("My dataset has > 1M rows")
    want_built_in_sorting = st.checkbox("I want built-in sorting")
    want_built_in_filtering = st.checkbox("I want built-in filtering")
    want_built_in_single_cell_editing = st.checkbox("I want built-in single cell editing")
    want_built_in_excel_formulas = st.checkbox("I want built-in Excel formulas")
    want_built_in_pivot_tables = st.checkbox("I want built-in pivot tables")
    want_edits_to_propogate_to_rest_of_app = st.checkbox("I want edits made to the grid to propogate to the rest of my app")
    want_automation = st.checkbox("I want to record user edits and reuse them on other datasets")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:

        st.markdown(f'''We reccomend you use 
            {get_grid_recconmendation(
            has_greater_than_50_rows, 
            has_greater_than_1M_rows, 
            want_built_in_sorting, 
            want_built_in_filtering, 
            want_built_in_excel_formulas, 
            want_built_in_pivot_tables,
            want_edits_to_propogate_to_rest_of_app,
            want_automation)}. 
        ''')


