import dash_bootstrap_components as dbc
import dash_html_components as html

from general_overview import tab_general_overview_content
from shared import app
from top_level_collapse import collapse, collapse_button

dashboard_logo_url = 'https://image.flaticon.com/icons/png/512/1111/1111512.png'
server = app.server

app.layout = dbc.Container([
    dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=dashboard_logo_url, height='30px')),
                        dbc.Col(dbc.NavbarBrand('Mental Health in Tech Dashboard', className='ml-2')),
                    ],
                    align='center',
                    no_gutters=True,
                ),
                href='https://github.com/UBC-MDS/dsci-532_group08',
            ),
            dbc.NavbarToggler(id='navbar-toggler'),
            dbc.Collapse(collapse_button, id='navbar-collapse', navbar=True)
        ],
        color='light', dark=False,
        style={
            'border-radius': '5px'
        }
    ),
    html.Br(),
    collapse,
    dbc.Row([
        dbc.Col([
            dbc.Tabs(
                [
                    dbc.Tab(tab_general_overview_content,
                            label='General Overview',
                            tab_id='tab-general-overview'),
                    dbc.Tab(label='Company Support',
                            tab_id='tab-company-support'),
                ],
                id='card-tabs',
                active_tab='tab-general-overview'
            )
        ])
    ]),
    html.Hr(),
    html.P('This dashboard was made by DSCI 532 Group 8, '
           'with contributors: Mitchie Zhao, Jordon Lau, Kaicheng Tan, Daniel Ortiz.',
           style={'font-size': '80%'}),
    html.P('Please refer to the repository URL for source code and license information: '
           'https://github.com/UBC-MDS/dsci-532_group08.',
           style={'font-size': '80%'})
], fluid=True, style={'border-width': '10'})

if __name__ == '__main__':
    app.run_server(debug=True)
