import os
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC

#to open a file
file_name= "MOD05_L2.A2020181.0330.061.2020181131404.hdf"
hdf= SD(file_name,SDC.READ)
# listing SDS datasets
print(hdf.datasets())

#selecting dataset 
DATAFIELD_NAME='Cloud_Mask_QA'
data3D = hdf.select(DATAFIELD_NAME)
data=data3D[:,:]
print('cloud_mask_QA_data : ', data)
        

#reading geolcation dataset
lat = hdf.select('Latitude')
latitude = lat[:,:]
print('Latitudes : ', latitude)
lon = hdf.select('Longitude')
longitude = lon[:,:]
print('Longitudes : ', longitude)

# ploting data of Cloud Mask QA data in map
m = Basemap(projection='cyl', resolution='l',
            llcrnrlat=-90, urcrnrlat = 90,
            llcrnrlon=-180, urcrnrlon = 180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x,y,data)
cb = m.colorbar()
cb.set_label('Unit:%')

plt.title('{0}\n {1} at H20PrsLvls=11'.format(FILE_NAME, DATAFIELD_NAME))
fig = plt.gcf()
# Show the plot window.
plt.show()
