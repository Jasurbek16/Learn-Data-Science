import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data
cc_pops = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_pops[code] = population

# Group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_pops.items():
    if pop < 100000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
# This gives you a light overall theme but bases the country colors on the
# color you pass as an argument.
wm = pygal.maps.world.World(style = wm_style)
# pygal chooses colors for each of the groups based on the color provided.
wm.title = 'World Population in 2010'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('World_Population.svg')

