import streamlit as st

st.title("Streamlit Data Grid Comparison")

st.markdown("""
            
## Motivation
            
Streamlit makes it easy to build and share data apps with your teammates. 
            
Of course, your teammates want a grid! At least, so says the past 40 years of Excel’s dominance.

Streamlit has a variety of built-in grid components, and there are a variety of third party grids as well.
            
This app, explores the most popular Streamlit grids, and discusses which are appropriate for your use case.

## The Contenders
            
- [Streamlit’s native `st.table`](https://docs.streamlit.io/library/api-reference/data/st.table)
- [Streamlit’s native `st.dataframe`](https://docs.streamlit.io/library/api-reference/data/st.dataframe)
- [Streamlit's native `st.data_editor`](https://docs.streamlit.io/library/api-reference/data/st.data_editor)
- [AgGrid for Streamlit](https://streamlit-aggrid.readthedocs.io)
- [Mito for Streamlit](https://docs.trymito.io/mito-for-streamlit/getting-started)
            

#### A disclaimer  

We’re the authors of the `Mito` package — but we’re doing our very best to stay unbiased! Mito is great for some use cases, but not others. 
            
Feel free to open a PR against this [repo](https://github.com/mito-ds/streamlit-grid-comparison) if you think we can represent any of the libraries here better.

""")