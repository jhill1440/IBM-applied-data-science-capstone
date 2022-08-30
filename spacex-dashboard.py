{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red157\green0\blue210;\red144\green1\blue18;\red0\green0\blue109;\red19\green118\blue70;\red0\green0\blue255;
\red101\green76\blue29;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c68627\c0\c85882;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c6275\c50196;\cssrgb\c3529\c52549\c34510;\cssrgb\c0\c0\c100000;
\cssrgb\c47451\c36863\c14902;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Import required libraries\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf0 \strokec4  pandas \cf5 \strokec5 as\cf0 \strokec4  pd\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  dash\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  dash_html_components \cf5 \strokec5 as\cf0 \strokec4  html\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  dash_core_components \cf5 \strokec5 as\cf0 \strokec4  dcc\cb1 \
\cf5 \cb3 \strokec5 from\cf0 \strokec4  dash.dependencies \cf5 \strokec5 import\cf0 \strokec4  Input, Output\cb1 \
\cf5 \cb3 \strokec5 import\cf0 \strokec4  plotly.express \cf5 \strokec5 as\cf0 \strokec4  px\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Read the airline data into pandas dataframe\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 spacex_df = pd.read_csv(\cf6 \strokec6 "spacex_launch_dash.csv"\cf0 \strokec4 )\cb1 \
\cb3 max_payload = spacex_df[\cf6 \strokec6 'Payload Mass (kg)'\cf0 \strokec4 ].max()\cb1 \
\cb3 min_payload = spacex_df[\cf6 \strokec6 'Payload Mass (kg)'\cf0 \strokec4 ].min()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Create a dash application\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 app = dash.Dash(\cf7 \strokec7 __name__\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Create an app layout\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 launch_sites = []\cb1 \
\cb3 launch_sites.append(\{\cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'All Sites'\cf0 \strokec4 , \cf6 \strokec6 'value'\cf0 \strokec4 : \cf6 \strokec6 'All Sites'\cf0 \strokec4 \})\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  item \cf5 \strokec5 in\cf0 \strokec4  spacex_df[\cf6 \strokec6 "Launch Site"\cf0 \strokec4 ].value_counts().index:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     launch_sites.append(\{\cf6 \strokec6 'label'\cf0 \strokec4 : item, \cf6 \strokec6 'value'\cf0 \strokec4 : item\})\cb1 \
\
\cb3 app.layout = html.Div(\cf7 \strokec7 children\cf0 \strokec4 =[html.H1(\cf6 \strokec6 'SpaceX Launch Records Dashboard'\cf0 \strokec4 ,\cb1 \
\cb3                                         \cf7 \strokec7 style\cf0 \strokec4 =\{\cf6 \strokec6 'textAlign'\cf0 \strokec4 : \cf6 \strokec6 'center'\cf0 \strokec4 , \cf6 \strokec6 'color'\cf0 \strokec4 : \cf6 \strokec6 '#503D36'\cf0 \strokec4 ,\cb1 \
\cb3                                                \cf6 \strokec6 'font-size'\cf0 \strokec4 : \cf8 \strokec8 40\cf0 \strokec4 \}),\cb1 \
\cb3                                 \cf2 \strokec2 # TASK 1: Add a dropdown list to enable Launch Site selection\cf0 \cb1 \strokec4 \
\cb3                                 \cf2 \strokec2 # The default select value is for ALL sites\cf0 \cb1 \strokec4 \
\cb3                                 \cf2 \strokec2 # dcc.Dropdown(id='site-dropdown',...)\cf0 \cb1 \strokec4 \
\cb3                                 dcc.Dropdown(\cf7 \strokec7 id\cf0 \strokec4 =\cf6 \strokec6 'site-dropdown'\cf0 \strokec4 , \cf7 \strokec7 options\cf0 \strokec4  = launch_sites, \cf7 \strokec7 value\cf0 \strokec4  = \cf6 \strokec6 'All Sites'\cf0 \strokec4 , \cf7 \strokec7 placeholder\cf0 \strokec4  = \cf6 \strokec6 "Select a Launch Site here"\cf0 \strokec4 , \cf7 \strokec7 searchable\cf0 \strokec4  = \cf9 \strokec9 True\cf0 \strokec4 ),\cb1 \
\cb3                                 html.Br(),\cb1 \
\
\cb3                                 \cf2 \strokec2 # TASK 2: Add a pie chart to show the total successful launches count for all sites\cf0 \cb1 \strokec4 \
\cb3                                 \cf2 \strokec2 # If a specific launch site was selected, show the Success vs. Failed counts for the site\cf0 \cb1 \strokec4 \
\cb3                                 html.Div(dcc.Graph(\cf7 \strokec7 id\cf0 \strokec4 =\cf6 \strokec6 'success-pie-chart'\cf0 \strokec4 )),\cb1 \
\cb3                                 html.Br(),\cb1 \
\
\cb3                                 html.P(\cf6 \strokec6 "Payload range (Kg):"\cf0 \strokec4 ),\cb1 \
\cb3                                 \cf2 \strokec2 # TASK 3: Add a slider to select payload range\cf0 \cb1 \strokec4 \
\cb3                                 \cf2 \strokec2 #dcc.RangeSlider(id='payload-slider',...)\cf0 \cb1 \strokec4 \
\cb3                                 dcc.RangeSlider(\cf7 \strokec7 id\cf0 \strokec4 =\cf6 \strokec6 'payload-slider'\cf0 \strokec4 , \cf7 \strokec7 min\cf0 \strokec4  = \cf8 \strokec8 0\cf0 \strokec4 , \cf7 \strokec7 max\cf0 \strokec4  = \cf8 \strokec8 10000\cf0 \strokec4 , \cf7 \strokec7 step\cf0 \strokec4  = \cf8 \strokec8 1000\cf0 \strokec4 , \cf7 \strokec7 value\cf0 \strokec4  = [min_payload, max_payload], \cf7 \strokec7 marks\cf0 \strokec4 =\{ \cf8 \strokec8 2500\cf0 \strokec4 : \{\cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 '2500 (Kg)'\cf0 \strokec4 \}, \cf8 \strokec8 5000\cf0 \strokec4 : \{\cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 '5000 (Kg)'\cf0 \strokec4 \}, \cf8 \strokec8 7500\cf0 \strokec4 : \{\cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 '7500 (Kg)'\cf0 \strokec4 \}\}),\cb1 \
\cb3                                 \cf2 \strokec2 # TASK 4: Add a scatter chart to show the correlation between payload and launch success\cf0 \cb1 \strokec4 \
\cb3                                 html.Div(dcc.Graph(\cf7 \strokec7 id\cf0 \strokec4 =\cf6 \strokec6 'success-payload-scatter-chart'\cf0 \strokec4 )),\cb1 \
\cb3                                 ])\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # TASK 2:\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Add a callback function for `site-dropdown` as input, `success-pie-chart` as output\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 @app.callback\cf0 \strokec4 ( Output(\cf7 \strokec7 component_id\cf0 \strokec4 =\cf6 \strokec6 'success-pie-chart'\cf0 \strokec4 , \cf7 \strokec7 component_property\cf0 \strokec4 =\cf6 \strokec6 'figure'\cf0 \strokec4 ),\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3                Input(\cf7 \strokec7 component_id\cf0 \strokec4 =\cf6 \strokec6 'site-dropdown'\cf0 \strokec4 , \cf7 \strokec7 component_property\cf0 \strokec4 =\cf6 \strokec6 'value'\cf0 \strokec4 )\cb1 \
\cb3 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Add computation to callback function and return graph\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 def\cf0 \strokec4  \cf10 \strokec10 select\cf0 \strokec4 (\cf7 \strokec7 inputt\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 if\cf0 \strokec4  inputt == \cf6 \strokec6 'All Sites'\cf0 \strokec4 :\cb1 \
\cb3         new_df = spacex_df.groupby([\cf6 \strokec6 'Launch Site'\cf0 \strokec4 ])[\cf6 \strokec6 "class"\cf0 \strokec4 ].sum().to_frame()\cb1 \
\cb3         new_df = new_df.reset_index()\cb1 \
\cb3         fig = px.pie(new_df, \cf7 \strokec7 values\cf0 \strokec4 =\cf6 \strokec6 'class'\cf0 \strokec4 , \cf7 \strokec7 names\cf0 \strokec4 =\cf6 \strokec6 'Launch Site'\cf0 \strokec4 , \cf7 \strokec7 title\cf0 \strokec4 =\cf6 \strokec6 'Total Success Launches by Site'\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 else\cf0 \strokec4 :\cb1 \
\cb3         new_df = spacex_df[spacex_df[\cf6 \strokec6 "Launch Site"\cf0 \strokec4 ] == inputt][\cf6 \strokec6 "class"\cf0 \strokec4 ].value_counts().to_frame()\cb1 \
\cb3         new_df[\cf6 \strokec6 "name"\cf0 \strokec4 ] = [\cf6 \strokec6 "Failure"\cf0 \strokec4 , \cf6 \strokec6 "Success"\cf0 \strokec4 ]\cb1 \
\cb3         fig = px.pie(new_df, \cf7 \strokec7 values\cf0 \strokec4 =\cf6 \strokec6 'class'\cf0 \strokec4 , \cf7 \strokec7 names\cf0 \strokec4 =\cf6 \strokec6 'name'\cf0 \strokec4 , \cf7 \strokec7 title\cf0 \strokec4 =\cf6 \strokec6 'Total Success Launches for '\cf0 \strokec4  + inputt)\cb1 \
\cb3     \cf5 \strokec5 return\cf0 \strokec4  fig\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # TASK 4:\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 @app.callback\cf0 \strokec4 ( Output(\cf7 \strokec7 component_id\cf0 \strokec4 =\cf6 \strokec6 'success-payload-scatter-chart'\cf0 \strokec4 , \cf7 \strokec7 component_property\cf0 \strokec4 =\cf6 \strokec6 'figure'\cf0 \strokec4 ),\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3                Input(\cf7 \strokec7 component_id\cf0 \strokec4 =\cf6 \strokec6 'site-dropdown'\cf0 \strokec4 , \cf7 \strokec7 component_property\cf0 \strokec4 =\cf6 \strokec6 'value'\cf0 \strokec4 ), Input(\cf7 \strokec7 component_id\cf0 \strokec4 =\cf6 \strokec6 'payload-slider'\cf0 \strokec4 , \cf7 \strokec7 component_property\cf0 \strokec4 =\cf6 \strokec6 'value'\cf0 \strokec4 ) \cb1 \
\cb3 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 def\cf0 \strokec4  \cf10 \strokec10 scatter\cf0 \strokec4 (\cf7 \strokec7 input1\cf0 \strokec4 , \cf7 \strokec7 input2\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf10 \strokec10 print\cf0 \strokec4 (input1)\cb1 \
\cb3     \cf10 \strokec10 print\cf0 \strokec4 (input2)\cb1 \
\cb3     \cf5 \strokec5 if\cf0 \strokec4  input1 == \cf6 \strokec6 'All Sites'\cf0 \strokec4 :\cb1 \
\cb3         new_df = spacex_df\cb1 \
\cb3         new_df2 = new_df[new_df[\cf6 \strokec6 "Payload Mass (kg)"\cf0 \strokec4 ] >= input2[\cf8 \strokec8 0\cf0 \strokec4 ]]\cb1 \
\cb3         new_df3 = new_df2[new_df[\cf6 \strokec6 "Payload Mass (kg)"\cf0 \strokec4 ] <= input2[\cf8 \strokec8 1\cf0 \strokec4 ]]\cb1 \
\cb3         fig2 = px.scatter(new_df3, \cf7 \strokec7 y\cf0 \strokec4 =\cf6 \strokec6 "class"\cf0 \strokec4 , \cf7 \strokec7 x\cf0 \strokec4 =\cf6 \strokec6 "Payload Mass (kg)"\cf0 \strokec4 , \cf7 \strokec7 color\cf0 \strokec4 =\cf6 \strokec6 "Booster Version Category"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 else\cf0 \strokec4 :\cb1 \
\cb3         new_df = spacex_df[spacex_df[\cf6 \strokec6 "Launch Site"\cf0 \strokec4 ] == input1]\cb1 \
\cb3         new_df2 = new_df[new_df[\cf6 \strokec6 "Payload Mass (kg)"\cf0 \strokec4 ] >= input2[\cf8 \strokec8 0\cf0 \strokec4 ]]\cb1 \
\cb3         new_df3 = new_df2[new_df[\cf6 \strokec6 "Payload Mass (kg)"\cf0 \strokec4 ] <= input2[\cf8 \strokec8 1\cf0 \strokec4 ]]\cb1 \
\cb3         \cf2 \strokec2 #new_df2 = new_df[new_df["Payload Mass (kg)"] >= input2[0] & new_df["Payload Mass (kg)"] <= input2[1]]\cf0 \cb1 \strokec4 \
\cb3         fig2 = px.scatter(new_df3, \cf7 \strokec7 y\cf0 \strokec4 =\cf6 \strokec6 "class"\cf0 \strokec4 , \cf7 \strokec7 x\cf0 \strokec4 =\cf6 \strokec6 "Payload Mass (kg)"\cf0 \strokec4 , \cf7 \strokec7 color\cf0 \strokec4 =\cf6 \strokec6 "Booster Version Category"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 return\cf0 \strokec4  fig2\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Run the app\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf0 \strokec4  \cf7 \strokec7 __name__\cf0 \strokec4  == \cf6 \strokec6 '__main__'\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     app.run_server()\cb1 \
}