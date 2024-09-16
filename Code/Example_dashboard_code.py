import numpy as np
import pandas as pd
from interfaccia import automatic, dashboard

np.random.seed(0)
# generation random number
x = np.arange(0, 100)
y = np.random.normal(size=100)
z = np.random.uniform(1, 10, size=100)
w = np.random.binomial(n=10, p=0.5, size=100)

# df
df1 = pd.DataFrame({'x': x, 'y': y, 'z': z, 'w': w})
df2 = pd.DataFrame(
    {'Category': np.random.choice(['A', 'B', 'C', 'D'], size=50), 'Values': np.random.randint(1, 10, size=50)})
df3 = pd.DataFrame({'Category': np.random.choice(['X', 'Y', 'Z'], size=10), 'Count': np.random.randint(1, 20, size=10)})
df4 = pd.DataFrame(
    {'x': np.linspace(0, 10, 50), 'y': np.sin(np.linspace(0, 10, 50)), 'z': np.cos(np.linspace(0, 10, 50))})


#######################################################################################################################
###################################              "Creation of charts and tables          ##############################
#######################################################################################################################

                                    ####################################################
                                 #### x_name AND y_name column in to df MUST BE STRING ####
                                    ####################################################

# CHART 1
chart_1, table_1 = automatic(
    df1,  # name of the df with the data
    columns=[
        ('x', 'y', 'Bar Data', 'bar', 'add_y'),
        # ('X axes column name',  'Y axes column name', 'name on legend', 'chart type', 'add_y') If you want to add the secondary y or x axis, just insert 'add_y' or 'add_x' at the end.
        ('w', 'z', 'Line Data', 'scatter', 'add_x')
        # ('X axes column name',  'Y axes column name', 'name on legend', 'chart type', 'add_x') If you want to add the secondary y or x axis, just insert 'add_y' or 'add_x' at the end.
    ],
    title='',  # title chart, If you don't want the axis to appear, simply leave it blank.
    xaxis_title='X Axis',  # title on X axes, If you don't want the axis to appear, simply leave it blank.
    yaxis_title='Y Axis',  # title on Y axes, If you don't want the axis to appear, simply leave it blank.
    note='Lorem ipsum dolor sit amet...'  # note chart
)

# CHART 2
chart_2, table_2 = automatic(
    df2,  # name of the df with the data
    columns=[
        ('Category', 'Values', 'pie Chart', 'pie')
        # ('X axis column name',  'Y axis column name', 'name on legend', 'chart type', 'add_y') If you want to add the secondary y or x axis, just insert 'add_y' or 'add_x' at the end.
    ],
    title='Lorem ipsum...',  # title on chart, If you don't want the axis to appear, simply leave it blank.
    xaxis_title='Category',  # title on X axis, If you don't want the axis to appear, simply leave it blank.
    yaxis_title='Values',  # title on Y axis, If you don't want the axis to appear, simply leave it blank.
    note='Lorem ipsum dolor sit amet....'  # note chart, If you don't want the axis to appear, simply leave it blank.
)

# CHART 3
chart_3, table_3 = automatic(
    df3,  # name of the df with the data
    columns=[
        ('Category', 'Count', 'Count Data', 'bar')  # Assuming columns in df3 are 'Category' and 'Count', and using a 'bar' chart.
    ],
    title='',  # title on chart, If you don't want the axis to appear, simply leave it blank.
    xaxis_title='Category',  # title on X axis, If you don't want the axis to appear, simply leave it blank.
    yaxis_title='Count',  # title on Y axis, If you don't want the axis to appear, simply leave it blank.
    note='Lorem ipsum dolor sit amet...'  # note chart, If you don't want the axis to appear, simply leave it blank.
)

chart_4, table_4 = automatic(
    df4,  # name of the df with the data
    columns=[
        ('x', 'y', 'Sine Function', 'scatter'),
        ('x', 'z', 'Cosine Function', 'scatter', 'add_y')  # add y axis
    ],
    title='',
    xaxis_title='X Axis',
    yaxis_title='Y Axis',
    note='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.'
)
#add more charts and DF


#######################################################################################################################
###################################              "Creation of charts and tables          ##############################
#######################################################################################################################
data = {  # data is the container where the dashboard filling data is stored.
    'navbar': {  # contaner navbar menù
        'brand_name': 'INTERFACCIA',  # name on the navebar,If you don't want the axis to appear, simply leave it blank.
        'subtitle': 'Interactive Dashboard',
        # subtitle on the navebar,If you don't want the axis to appear, simply leave it blank.
        'menu_items': [  # pages on the navbar menu'
            {'id': 'home', 'label': 'Home'},
            # You can choose not to include 'Home' as a menu item because the title acts as a button for the home page. Id should be unique NOT STABLE
            {'id': 'abc', 'label': 'Page'},  # single page on menù. Id should be unique
            {'id': 'abcd', 'label': 'Drop menù', 'submenu': [  # page with subpage on menù, Id should be unique
                {'id': 'abcde', 'label': 'page 1'},  # subpage 1, Id should be unique
                {'id': 'abcdef', 'label': 'Page 2'},  # subpage 3, Id should be unique
            ]},
        ]
    },
    'pages': [  # contaner all page
        {
            'id': 'home',  # id connect with the id of navbar
            'type': 'home',  # home #You can choose between three types of pages: home, page, and page_menu.
            'title': 'Welcome to the Interfaccia Example',  # title page
            'image_src': 'https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/interfaccia_1.png',
            # link for image page
            'contents': [  # contaneir for the content page
                {"type": "home",  # type of layout page
                 "id": "Home",  # Id page
                 "content": '<p>'  # text on the home page 
                            'This <a href="https://github.com/fr-cm/interfaccia">repository</a>'
                            ' is designed to streamline the process of creating a modular, multi-device '
                            'dashboard with simulated interactivity while minimizing Python code. '
                            'It features functions that automate the creation of charts and tables, '
                            'and it provides automatic download links for CSV files, allowing users to '
                            'download data without the need for server storage. Additionally, it addresses'
                            ' the issue of resizing Plotly charts when display is set to none. Check out the '
                            'pages below to explore its various features and capabilities.
                            '</p>'}
            ]
        },
        {
            'id': 'abc',  # id connect with the id of navbar
            'type': 'page_menu',  # page_menu #You can choose between three types of pages: home, page, and page_menu.
            'title': 'Page Menù',  # title page
            'contents': [  # contaneir for the content page
                {"id": "id-content",  # id content for menù. Id must be unique
                 "type": "plot_table_download",  # type of layout page
                 "label": "chart one",  # title on the dropdown menù
                 "plot": chart_1,  # unique name of chart
                 "data": table_1,  # unique name of table
                 'display': 'block'  # first content of page_manù must be 'block' the other, must be 'none'
                 },
                {"id": "id-content-one",  # #id content for menù. Id must be unique
                 "type": "plot_table_download",  # type of layout page
                 "label": "chart one",  # title on the dropdown menù
                 "plot": chart_2,  # unique name of chart
                 "data": table_2,  # unique name of table
                 'display': 'none'  # first content of page_manù must be 'block' the other, must be 'none'
                 },
                {"id": "id-content-2",  # id content for menù. Id must be unique
                 "type": "plot_table_download",  # type of layout page
                 "label": "chart one",  # title on the dropdown menù
                 "plot": chart_3,  # unique name of chart
                 "data": table_3,  # unique name of table
                 'display': 'none'  # first content of page_manù must be 'block' the other, must be 'none'
                 },
            # add more contents
            
            ]
        },

        {
            'id': 'abcde',  # id connect with the id of navbar
            'type': 'page',  # page  # You can choose between three types of pages: home, page, and page_menu.
            'title': 'Page One',  # title page
            'contents': [  # contaneir for the content page
                {"id": "id-content-5",  # id content page  Id must be unique
                 "type": "plot_download",  # type of layout page
                 "title": "chart one",  # title page
                 "plot": chart_4,  # unique name of chart
                 'display': 'block'
                 },
                {"id": "id-content-8",  # id content page  Id must be unique
                 "type": "table",  # type of layout page
                 "title": "chart one",  # title page
                 "data": table_4,  # unique name of table
                 'display': 'block'
                 },
            ]
        },
        {
            'id': 'abcdef',  # id connect with the id of navbar
            'type': 'page',  # page  # You can choose between three types of pages: home, page, and page_menu.
            'title': 'Page Two',  # title page
            'contents': [  # contaneir for the content page
                {"type": "txt_img",  # type of layout page
                 'image_src': 'https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/img_1.png',
                 # link image
                 "title": "<h3> Lorem sed iaculis leo dictum. </h3>",  # title text
                 "text": "<p> "  # text
                         "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, "
                         "mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. "
                         "Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. "
                         "Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. "
                         "Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. "
                         "Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. "
                         "Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. "
                         "</p>",
                 }]
        },
        # add more pages
        {
            'id': 'footer',# id connect
            'type': 'footer',#footer
            'contents': [# contaneir for the content page
                {"type": "footer", # type of layout page
                 "text": "<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, </p>\n" #text
                 }]
        }

    ]
}
#######################################################################################################################
###################################              "Creation of charts and tables          ##############################
#######################################################################################################################
dashboard(name='Example_Dashboard.html', #Name you want to give the file
          input=r'C:\...\...\...\template_interfaccia.html', #directory where the template file is stored
          output=r'C:\...\...\...\...', #directory where you want the file to be saved
          data=data)#container with all the template data


