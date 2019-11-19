
import plotly.graph_objects as go
import pandas
import plotly.io as pio


sex = 'Persons'
group = 'DALYs 15-29'
z = 'daly_norm_pm'
ghe = 540
dalys = pandas.read_csv('DALYs_15-29.csv')

select = dalys.query('sex == @sex')
select = select.query('group == @group')
select = select.query('GHE == @ghe')


#pio.renderers.default = "png"


fig = go.Figure(data=go.Choropleth(
    locations=select['country'], # Spatial coordinates
    z = select[z], # Data to be color-coded
    locationmode = "country names", # set of locations match entries in `locations`
    colorscale = 'hot',
    colorbar_title = "Millions USD",
))

latitude = dict(range=[20, 60],showgrid=True, dtick=10)
longitude = dict(range=[-100, 20],showgrid=True,dtick=20)
geo = dict(lataxis= latitude, lonaxis = longitude)

fig.update_layout(
    title_text = 'Nutrition Deficiencies',
    #geo_scope='world', # limit map scope to US
    geo = geo
)

#fig.show()
fig.write_image("fig1.png")

