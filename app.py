import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import matplotlib
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

st.set_page_config(
    page_title="Use Maps In Streamlit",
    layout="wide"
)

st.title("Use Maps In Streamlit")

@st.cache_data
def get_df() -> pd.DataFrame:
    df = pd.read_csv('data/geodata.csv')
    return df

df = get_df()

def plot_column(selected_column):
    # Normalize the values in the 'Lot Area' column to the range [0, 1]
    norm = mcolors.Normalize(vmin=df[selected_column].min(), vmax=df[selected_column].max())

    # Map the normalized values to colors using the 'viridis' color map
    cmap = matplotlib.colormaps.get_cmap('YlGn')
    colors = cmap(norm(df[selected_column]))

    hex_colors = [mcolors.to_hex(color) for color in colors]

    # Add the colors to the DataFrame
    df['color'] = hex_colors
    return norm, cmap 

option = st.selectbox(
   "Select values to plot",
   df.select_dtypes(include=np.number).columns.tolist(),
   index=5,
   placeholder="Select values to plot",
)

norm, cmap = plot_column(option)

st.map(df,
    latitude='lat',
    longitude='lng',
    size=5,
    color='color')

# fig, ax = plt.subplots()
# cax = fig.add_axes([0.27, 0.8, 0.5, 0.05]) # Add an axes for the color bar

# # Create a color bar
# cb = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax)

# st.pyplot(fig) # Display the figure with the color bar

fig, ax = plt.subplots()
cax = fig.add_axes([0.27, 0.8, 0.5, 0.05]) # Add an axes for the color bar

# Create a color bar
cb = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation='horizontal')

ax.axis('off')

st.pyplot(fig) # Display the figure with the color bar