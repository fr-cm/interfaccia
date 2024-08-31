
#####################################################################################
#####################################################################################
#####################################################################################
########################              interfaccia                ######################
#####################################################################################
########################               created by              ######################
########################               F. CAMASSA              ######################
#####################################################################################
#####################################################################################
#####################################################################################

import plotly.graph_objs as go
import plotly.io as pio
from jinja2 import Environment, FileSystemLoader

#####################################################################################
########################               automatic               ######################
#####################################################################################
def create_column(x, y, label, chart_type='scatter', add_x=None, add_y=None):
    """
    Facilitates the writing for multi-track charts; the function is integrated automatically.

    Parameters:
    - x: Name of the column for the x-axis
    - y: Name of the column for the y-axis
    - label: Label for the legend
    - chart_type: Type of chart ('scatter', 'bar', 'area', 'pie')
    - add_x: If 'add_x', use the secondary x-axis
    - add_y: If 'add_y', use the secondary y-axis
    """
    return {'x': x, 'y': y, 'label': label, 'chart_type': chart_type, 'add_x': add_x, 'add_y': add_y}

def automatic(df, columns, title='', xaxis_title='', yaxis_title='', note="", **kwargs):
    """
    Creates a customizable plotly chart from a DataFrame using multiple chart types.

    Parameters:
    - df: pandas DataFrame containing the data to be plotted.
    - columns: List of tuples where each tuple specifies the columns
        in the DataFrame to plot, the chart type, and optional x and
        y axis additions. Each tuple should be in the form
        (x_name, y_name, label, chart_type, [add_x, add_y]).
    - title: Title of the chart (default is an empty string).
    - xaxis_title: Title for the x-axis (default is an empty string).
    - yaxis_title: Title for the y-axis (default is an empty string).
    - note: Text to be used in annotations (default is an empty string).
    - **kwargs: Additional keyword arguments for customizing the layout.

        columns parameters:
         - x: Name of the column for the x-axis
         - y: Name of the column for the y-axis
         - label: Label for the legend
         - chart_type: Type of chart ('scatter', 'bar', 'area', 'pie')
         - add_x: If 'add_x', use the secondary x-axis
         - add_y: If 'add_y', use the secondary y-axis
    """

    full_palette = [# color parameters
        '#00379f', '#007eff', '#7bd200', '#35009f', '#0174af',
        '#db5700', '#bbd64a', '#a9a3d0', '#007eff', '#7bd200',
        '#db5700', '#ffc000', '#403152', '#bfbfbf', '#00b050',
        '#cc66cd', '#00379f', '#00b0f0', '#92cddc'
    ]

    pio.templates['custom_theme'] = go.layout.Template(# set and application custom template
        layout=go.Layout(
            colorway=full_palette,
            font={'family': "Arial"}
        )
    )
    pio.templates.default = 'custom_theme'

    chart_funcs = { # Plot map
        'scatter': go.Scatter,
        'bar': go.Bar,
        'area': go.Scatter,
        'pie': go.Pie
    }

    traces = []
    secondary_x = False
    secondary_y = False

    for col in columns:#data list plot
        x_name = col[0]
        y_name = col[1]
        label = col[2]
        chart_type = col[3]
        add_x = col[4] if len(col) > 4 else None
        add_y = col[5] if len(col) > 5 else None

        ###################################
        # x_name AND y_name MUST BE STRING#
        ###################################

        if not isinstance(x_name, str) or not isinstance(y_name, str):
            raise ValueError("x_name and y_name must be strings")

        if x_name not in df.columns:
            raise KeyError(f"Column '{x_name}' not found in DataFrame")
        if y_name not in df.columns:
            raise KeyError(f"Column '{y_name}' not found in DataFrame")

        color = full_palette[len(traces) % len(full_palette)]# color allocation

        if chart_type == 'scatter':
            trace = go.Scatter(
                x=df[x_name],
                y=df[y_name],
                name=label,
                line={'color': color, 'width': 1},
                mode='lines',
                yaxis='y2' if add_y == 'add_y' else 'y',
                xaxis='x2' if add_x == 'add_x' else 'x'
            )
        elif chart_type == 'bar':
            trace = go.Bar(
                x=df[x_name],
                y=df[y_name],
                name=label,
                marker={'color': color},
                width=1,
                orientation='v',
                yaxis='y2' if add_y == 'add_y' else 'y',
                xaxis='x2' if add_x == 'add_x' else 'x'
            )
        elif chart_type == 'area':
            trace = go.Scatter(
                x=df[x_name],
                y=df[y_name],
                name=label,
                line={'color': color, 'width': 1},
                mode='lines',
                fill='tozeroy',
                yaxis='y2' if add_y == 'add_y' else 'y',
                xaxis='x2' if add_x == 'add_x' else 'x'
            )
        elif chart_type == 'pie':
            trace = go.Pie(
                labels=df[x_name],
                values=df[y_name],
                name=label,
                marker={'colors': None},
                hole=0
            )
        else:
            raise ValueError(f"Unsupported plot type: {chart_type}")

        traces.append(trace)

        if add_x == 'add_x':
            secondary_x = True
        if add_y == 'add_y':
            secondary_y = True

    fig = go.Figure(data=traces)# plot generation

    fig.update_layout( # general costum template
        title=title,
        title_x=0.5,
        xaxis=dict(title=xaxis_title, tickmode='array'),
        yaxis=dict(title=yaxis_title),
        autosize=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            x=0.5,
            y=1.15,
            xanchor='center',
            yanchor='top',
            orientation='h'
        ),
        annotations=[{
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': -0.2,
            'text': note,
            'showarrow': False,
            'font': {'size': 10, 'color': 'gray'},
            'align': 'center',
            'xanchor': 'center',
            'yanchor': 'top'
        }]
    )

    if secondary_x:
        fig.update_layout(
            xaxis2=dict(
                overlaying='x',
                side='top'
            )
        )
    if secondary_y:
        fig.update_layout(
            yaxis2=dict(
                overlaying='y',
                side='right'
            )
        )

    fig.update_layout(**kwargs)

    fig_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')# Plot Conversion to HTML

    df_html = df.to_html(index=False).replace('\n', '') # DataFrame conversion to HTML
    return fig_html, df_html


#####################################################################################
########################               dashboard               ######################
#####################################################################################


def dashboard(name, input, output, data):
    """
    This script generates an HTML file using a template and a set of data.

    Parameters:
    - name: The name of the HTML file to be created (e.g., 'dashboard.html').
    - input: The path to the HTML template to use ('easy_template.html').
    - output: The directory path where the generated HTML file will be saved.
    - data: The content for the dashboard.
    """

    template_dir = input.rsplit('\\', 1)[0]
    template_name = input.rsplit('\\', 1)[1]
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    html_output = template.render(data=data)
    output_path = f"{output}\\{name}"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"You can find your dashboard in: {output_path}")

