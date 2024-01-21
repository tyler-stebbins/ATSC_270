#
#
from siphon.simplewebservice.iastate import IAStateUpperAir
from metpy.io import add_station_lat_lon
import datetime
import pandas

# get_raobs 
# returns a pandas dataframe with RAOBs
# input = dt (a datetime object)


# select_press
# returns a pandas dataframe with RAOB observations at the specified pressure level
# input = data (a RAOB pandas dataframe)
#       = press_lev (the pressure level requested in hPa)


