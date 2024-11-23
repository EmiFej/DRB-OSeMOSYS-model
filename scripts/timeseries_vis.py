import random
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# Function to generate random color in hex format
def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Function to generate the interactive plot
def plot_timeseries(df, 
                    countries_gdf, 
                    save_path,
                    plot_title):
    # Create a subplot grid with 3 rows and 1 column
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,  # Share x-axis across rows
        vertical_spacing=0.1,  # Adjust the space between the plots
        subplot_titles=[f'Hourly Timeseries for {countries_gdf.loc[column]["Country"]}' for column in df.columns]
    )

    # Add each region's timeseries to the respective subplot
    for i, column in enumerate(df.columns):
        fig.add_trace(
            go.Scatter(x=df.index, y=df[column], 
                       mode='lines', name=column,
                       line=dict(color=random_color())),  # Random color for each line
            row=i+1, col=1
        )

    # Update layout for dark theme and appearance
    fig.update_layout(
        template="plotly_dark",  # Apply dark theme
        title_font=dict(size=16, color='white'),  # Title font color
        xaxis_title_font=dict(size=12, color='white'),
        yaxis_title_font=dict(size=12, color='white'),
        xaxis=dict(showgrid=True, gridcolor='gray'),  # Grid lines for x-axis
        yaxis=dict(showgrid=True, gridcolor='gray'),
        plot_bgcolor='black',  # Background color
        margin=dict(t=40, b=40, l=50, r=50),  # Margins
        yaxis_title="GW",  # Set the Y-axis title to "GW"
        showlegend=False,  # Disable legend if not needed
        title=plot_title,  # Add a super title "Solar"
    )

    # Ensure the parent directory exists for saving
    plot_save_to = Path(save_path)
    plot_save_to.parent.mkdir(parents=True, exist_ok=True)

    # Save the combined plot to an HTML file
    fig.write_html(plot_save_to)

    # Show the combined plot
    fig.show()


