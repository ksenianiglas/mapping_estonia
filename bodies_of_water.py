import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap

fig= plt.figure(figsize=(20,20))
ax= fig.add_subplot(111)

#initiate a basemap layer
m = Basemap(
    resolution = 'l',
    projection = 'merc',
    #coordinates of the corners - lower left lat/lon and upper right lat/lon
    llcrnrlat=57.4,llcrnrlon=21.5,
           urcrnrlat=59.8,urcrnrlon=28.7);

#fill in the background
m.drawmapboundary(fill_color='#1c1c1c')
m.fillcontinents(color='#1c1c1c',lake_color='#1c1c1c');

#I downloaded the .shp.zip archive for Estonia from http://download.geofabrik.de/
#and placed the files in a subfolder "geo"
m.readshapefile('geo/gis_osm_water_a_free_1', 'waterways', drawbounds = False,
                color='#1c1c1c')
#Determine polygons to fill in (in this case they will be lakes, rivers, etc)
patches   = []
for info, shape in zip(m.waterways_info, m.waterways):
    patches.append( Polygon(np.array(shape), True) )


#fill in the polygons        
ax.add_collection(PatchCollection(patches, facecolor= '#5f8999', edgecolor='#5f8999', linewidths=1., zorder=2))

plt.savefig('Estonia_bodies_of_water')
