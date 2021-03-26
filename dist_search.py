from math import radians, cos, sin, asin, sqrt

class DistSearch:
    def __init__(self,lat1, lat2, lon1, lon2):
        self.lat1 = lat1
        self.lat2 = lat2
        self.lon1 = lon1
        self.lon2 = lon2

    def distance(self):
        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(self.lon1)
        lon2 = radians(self.lon2)
        lat1 = radians(self.lat1)
        lat2 = radians(self.lat2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        # calculate the result
        return (c * r)


#lat1 = 51.5074
#lat2 =48.8566
#lon1 = 0.1278
#lon2 = 2.3522
lat1 = float(input("City 1 latitude"))
lon1 = float(input("City 1 longitude"))
lat2 = float(input("City 2 latitude"))
lon2 = float(input("City 2 longitude"))

obj = DistSearch(lat1,lat2,lon1,lon2)
s = obj.distance()
# driver code
print("City 1 and City 2 are {:.2f} km apart".format(s))

#print(distance(lat1, lat2, lon1, lon2), "K.M")