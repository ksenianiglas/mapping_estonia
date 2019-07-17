import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(20,20))

#initiate a basemap layer
m = Basemap(
    resolution = 'l',
    projection = 'merc',
    #coordinates of the corners - lower left lat/lon and upper right lat/lon
    llcrnrlat=57.4,llcrnrlon=21.5,
           urcrnrlat=59.8,urcrnrlon=28.5);

#fill in the background
m.drawmapboundary(fill_color='#1c1c1c')
m.fillcontinents(color='#1c1c1c',lake_color='#1c1c1c');

#I downloaded the .shp.zip archive for Estonia from http://download.geofabrik.de/
#and placed the files in a subfolder "geo"
m.readshapefile('geo/gis_osm_roads_free_1', 'roads', drawbounds = True,
                color='#b8b8b8')

plt.savefig('estonian_roads')
