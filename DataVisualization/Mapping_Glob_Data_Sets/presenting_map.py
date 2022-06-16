import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', {'ca': 3651531, 'mx':45155421, 'us':5552252})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('DataVisualization\\Mapping_Glob_Data_Sets\\N_C_S_America.svg')

# Pygal automatically uses these numbers to
# shade the countries from light (least populated) to dark (most populated).











