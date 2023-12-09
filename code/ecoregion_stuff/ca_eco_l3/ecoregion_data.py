# import geopandas as gpd
# import inline
# import matplotlib
#
# fp ="ca_eco_l3.shp"
# data = gpd.read_file(fp)
#
# print(data.head(2))
#
# %matplotlib inline
# data.plot()

import matplotlib.pyplot as plt
import shapefile

shpFilePath = "/ca_eco_l3.shp"
listx=[]
listy=[]
test = shapefile.Reader(shpFilePath)
for sr in test.shapeRecords():
    for xNew,yNew in sr.shape.points:
        listx.append(xNew)
        listy.append(yNew)
plt.plot(listx,listy)
plt.show()