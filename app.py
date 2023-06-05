import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate timestamps for 3 years (365 days * 3 years)
timestamps = pd.date_range(start='2019-01-01', end='2021-12-31', freq='D')

# Create an empty DataFrame to store the data
df = pd.DataFrame(columns=['Timestamp', 'Well', 'Oil Production'])

# Generate data for each well
for well_id in range(1, 11):
    # Generate random oil production values for each timestamp
    oil_production = np.random.randint(low=100, high=1000, size=len(timestamps))
    
    # Create a DataFrame for the well data
    well_df = pd.DataFrame({
        'Timestamp': timestamps,
        'Well': f'Well {well_id}',
        'Oil Production': oil_production
    })
    
    # Append the well data to the main DataFrame
    df = df.append(well_df, ignore_index=True)

# Save the dataset to a CSV file
df.to_csv('oil_well_production.csv', index=False)
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Load the dataset
df = pd.read_csv('oil_well_production.csv')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1('Oil Well Production Dashboard'),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='Timestamp', y='Oil Production', color='Well')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server()
