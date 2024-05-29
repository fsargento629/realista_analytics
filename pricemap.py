import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your dataset
df = pd.read_csv('data/listings_2024_05_21_21_16_03.csv')

# Filter outliers
df = df[df['price'] < 2e6] # less than 2million
df = df[df['pricePerM2'] < 20000] # less price per swr meter than 20k

# Initialize the map figure
fig = go.Figure()

# Add a scattermapbox layer for the house locations
fig.add_trace(go.Scattermapbox(
    lat=df['lat'],
    lon=df['lon'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=9,
        color=df['pricePerM2'],
        colorscale='Viridis',  # You can choose other colorscales as well
        colorbar=dict(title="Preço por m2")
    ),
    text=df['pricePerM2'],  # This will show the price on hover
))

# Update the layout to center the map and set the style
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_center={"lat": df['lat'].mean(), "lon": df['lon'].mean()},
    mapbox_zoom=10,
    title="Preço por m2 dos imóveis em Lisboa"
)

# Show the figure
fig.show()
