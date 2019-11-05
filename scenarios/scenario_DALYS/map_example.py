import plotly.graph_objects as go
import pandas
import plotly.io as pio


sex = 'Persons'
group = 'DALYs 70+'
z = 'daly_norm_pm'
ghe = 540
dalys = pandas.read_csv('DALYS.csv')

select = dalys.query('sex == @sex')
select = select.query('group == @group')
select = select.query('GHE == @ghe')


pio.renderers.default = "browser"


fig = go.Figure(data=go.Choropleth(
    locations=select['country'], # Spatial coordinates
    z = select[z], # Data to be color-coded
    locationmode = "country names", # set of locations match entries in `locations`
    colorscale = 'hot',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = 'empty',
    geo_scope='world', # limite map scope to USA
)

fig.show()
fig.write_image("fig1.pdf")

