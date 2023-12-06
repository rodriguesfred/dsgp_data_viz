import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Use Pygwalker In Streamlit(support communication)")

# Initialize pygwalker communication
init_streamlit_comm()

# When using `use_kernel_calc=True`, you should cache your pygwalker html, if you don't want your memory to explode
@st.cache_resource
def get_pyg_html(df: pd.DataFrame) -> str:
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    # If you want to use feature of saving chart config, set `debug=True`
    html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
    return html

@st.cache_data
def get_df() -> pd.DataFrame:
    return pd.read_csv('cleaned_data.to_csv('data/geodata.csv')')

df = get_df()

st.map(df,
    latitude='lat',
    longitude='lng',
    size=5,
    color='price_sq2')

components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)
