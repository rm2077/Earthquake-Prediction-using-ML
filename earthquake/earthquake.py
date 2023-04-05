import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import sklearn
from sklearn.linear_model import LinearRegression
import tensorflow as tf
import keras 




data = pd.read_csv('query (7).csv', sep=',')
mag = data['mag']
depth = data['depth']

#plt.plot(mag, depth, color='blue', marker="o", markersize = 2)
#plt.axis('tight')
#plt.xlabel('Magnitude')
#plt.ylabel('Depth')
#plt.title('Magnitude vs Depth')
#plt.show()
def MagDepth():
  ax = data.plot(x='longitude', y='latitude', colorbar="Blue", kind="scatter", c='mag')

  ax.set_xlabel('Longitude')
  ax.set_ylabel("Latitude")
  ax.set_title("Location vs Magnitude")
  ax.set_xticks(range(-180, 180, 40))
  ax.set_yticks(range(-70, 70, 10))

  plt.show()




def LatLong():
  data.plot(x='longitude', y='latitude', kind='scatter', colorbar='Red', c='longitude')
  plt.xlabel('Longitude')
  plt.ylabel('Latitude')
  plt.title("Earthquake Long Lats")
  plt.show()



def MagnitudeDepth():
  data.plot(x='depth', y='mag', kind="scatter")
  plt.xlabel('depth')
  plt.ylabel('magnitude')
  plt.title("Depth magnitude correlation")
  plt.show()





def drawMap():

  fig = plt.figure(figsize=(8,8))
  m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')


  m.drawcoastlines()
  m.fillcontinents(color='coral', lake_color = "blue")
  m.drawmapboundary()
  m.drawcountries()
  m.drawparallels(range(-90, 91, 30), labels=[1,0,0,0], fontsize=10)
  m.drawmeridians(range(-180, 181, 45), labels=[0,0,0,1], fontsize=10)


  longitudes = data['longitude']
  latitudes = data['latitude']
  x, y = m(longitudes, latitudes)
  m.plot(x, y, "o", markersize = 2, color = "r")

  plt.title("Earthquakes")

  plt.show()


def cleanData():
  data = data[['latitude', 'longitude', 'depth', 'mag']]
  



class LinearRegression():



  def __init__(self, x_test, y_test, x_train, y_train):
    self.x_train = x_train
    self.x_test = x_test
    self.y_train = y_train
    self.y_test = y_test
    self.x = np.array(data[['latitude', 'longitude']])
    self.y = np.array(data[['mag', 'depth']])
    



  def linear_regression(self):
    linear = LinearRegression()
    self.x_train, self.x_test, self.y_train, self.y_test = linear()







def main():
  pass

main()


