import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import matplotlib
import matplotlib.colors as mcolors

st.set_page_config(
    page_title="Use Maps In Streamlit",
    layout="wide"
)

st.title("Use Maps In Streamlit")

@st.cache_data
def get_df() -> pd.DataFrame:
    df = pd.read_csv('data/geodata.csv')
    df = df


    # Normalize the values in the 'Lot Area' column to the range [0, 1]
    norm = mcolors.Normalize(vmin=df['price_sq2'].min(), vmax=df['price_sq2'].max())

    # Map the normalized values to colors using the 'viridis' color map
    cmap = matplotlib.colormaps.get_cmap('YlGn')
    colors = cmap(norm(df['price_sq2']))

    hex_colors = [mcolors.to_hex(color) for color in colors]

    # Add the colors to the DataFrame
    df['color'] = hex_colors
    return df
df = get_df()

st.map(df,
    latitude='lat',
    longitude='lng',
    size=5,
    color='color')

# components.html(get_pyg_html(st.map), width=1300, height=1000, scrolling=True)
