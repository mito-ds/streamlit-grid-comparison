# streamlit-grid-comparison
Creating a Streamlit app and want to display data to your users? There are several Streamlit grid that you can choose from. 

This Streamlit apps compares the grid options available to help you decide which one is best for your app. 

## The grid options
- [Streamlit’s native `st.table`](https://docs.streamlit.io/library/api-reference/data/st.table)
- [Streamlit’s native `st.dataframe`](https://docs.streamlit.io/library/api-reference/data/st.dataframe)
- [Streamlit's native `st.data_editor`](https://docs.streamlit.io/library/api-reference/data/st.data_editor)
- [AgGrid for Streamlit](https://streamlit-aggrid.readthedocs.io)
- [Mito for Streamlit](https://docs.trymito.io/mito-for-streamlit/getting-started)

### Running this app locally

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run Grid\ Comparison.py
```