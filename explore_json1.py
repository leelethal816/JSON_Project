import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readdable_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=5)

print(type(eq_data))

print(len(eq_data["features"]))

mags, lats, lons = [], [], []

for index in range(len(eq_data["features"])):
    mags.append(eq_data["features"][index]["properties"]["mag"])
    lons.append(eq_data["features"][index]["geometry"]["coordinates"][0])
    lats.append(eq_data["features"][index]["geometry"]["coordinates"][1])

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

my_data = Scattergeo(lon=lons, lat=lats)
my_layout = Layout(title="Global Earthquakes")

fig = {"data": my_data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
