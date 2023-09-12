import streamlit as st

st.title("Streamlit Data Grid Comparison")

st.markdown("""
            
## Motivation
            
Streamlit makes it easy to share data apps with your team. But as the last 40 years of Excel's dominance has shown, your teammates want a grid!
            
Streamlit has a variety of built-in grid components, and there are a variety of third party libraries that provide grids as well. 
            
This app is designed to help you choose the right grid for your app. To use this app:
1. Explore the different grids in the sidebar
2. Use the Which Grid is Right for Me? section to help you choose the right grid for your app

## The Contenders
            
- [Streamlit’s native `st.table`](https://docs.streamlit.io/library/api-reference/data/st.table)
- [Streamlit’s native `st.dataframe`](https://docs.streamlit.io/library/api-reference/data/st.dataframe)
- [Streamlit's native `st.data_editor`](https://docs.streamlit.io/library/api-reference/data/st.data_editor)
- [AgGrid for Streamlit](https://streamlit-aggrid.readthedocs.io)
- [Mito for Streamlit](https://docs.trymito.io/mito-for-streamlit/getting-started)
            

#### A disclaimer  

We’re the authors of the `Mito` package — but we’re doing our very best to stay unbiased! Mito is great for some use cases, but isn't a great fit for others. 
            
Feel free to open a PR against this [repo](https://github.com/mito-ds/streamlit-grid-comparison) if you think we can represent any of the libraries here better.
""")