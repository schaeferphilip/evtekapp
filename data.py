from geopy.geocoders import Nominatim
import geopy
import geopy.distance

import csv

with open('Route.csv', newline='') as f:
    reader = csv.reader(f)
    csvcords = [tuple(row) for row in reader]

print(csvcords)



geolocator = Nominatim(user_agent="my_user_agent")

locations = [
    "324 Plymouth Ave,Brightwaters,NY,11718",
    "539 Manatuck Blvd,Brightwaters,NY,11718",
    "131 S Windsor Ave,Brightwaters,NY,11718",
    "500 Peters Blvd,Brightwaters,NY,117182",
    "534 Brooklyn Blvd,Brightwaters,NY,11718",
    "915 Hiawatha Dr,Brightwaters,NY,11718",
    "68 Orinoco Dr,Brightwaters,NY,11718",
    "550 Lombardy Blvd,Brightwaters,NY,11718",
    "207 Plymouth Ct,Brightwaters,NY,11718",
    "427 Mayflower Ave,Brentwood,NY,11717",
    "33 Poplar St,Brentwood,NY,11717",
    "21 Virgil Dr,Brentwood,NY,11717",
    "141 Wittberg St,Brentwood,NY,11717",
    "65 Walton St,Brentwood,NY,11717",
    "154 Washington Ave,Brentwood,NY,11717",
    "1 Franklin St,Brentwood,NY,11717",
    "22 Doolittle St,Brentwood,NY,11717",
    "19 Laurie Rd,Brentwood,NY,11717",
    "1722 Church St,Bohemia,NY,11716",
    "110 Norman Dr,Bohemia,NY,11716",
    "1284 Church St,Bohemia,NY,11716",
    "780 Fulton Ave,Bohemia,NY,11716",
    "526 Walnut Ave,Bohemia,NY,11716",
    "9 Windwood Rd,Bohemia,NY,11716",
    "1065 Smithtown Ave,Bohemia,NY,11716",
    "247 Pond Rd,Bohemia,NY,11716",
    "23 Kathy Ln,Bohemia,NY,11716",
    "178 Division Ave,Blue Point,NY,11715",
    "62 Harbour Dr,Blue Point,NY,11715",
    "12 Edwards Ln,Blue Point,NY,11715",
    "6 Edwards Ln,Blue Point,NY,11715",
    "106 Namkee Rd,Blue Point,NY,11715",
    "211 Atlantic Ave,Blue Point,NY,11715",
    "62 Oyster Cove Ln,Blue Point,NY,11715",
    "14 Rebel Dr,Blue Point,NY,11715",
    "62 Harbour Dr,Blue Point,NY,11715",
    "50 W Millpage Dr,Bethpage ,NY,11714",
    "249 N 5th St,Bethpage ,NY,11714",
    "3 Northampton Gate,Bethpage ,NY,11714",
    "12 Floral Ave,Bethpage ,NY,11714",
    "213 S Pershing Ave,Bethpage ,NY,11714",
    "291 Sundown Dr,Bethpage ,NY,11714",
    "229 N 5th St,Bethpage ,NY,11714",
    "40 William St,Bethpage ,NY,11714",
    "11 Lincoln Rd,Bethpage ,NY,11714",
    "82 Bieselin Rd,Bellport,NY,11713",
    "10 Price St,Bellport,NY,11713",
    "815 Bellport Ave,Bellport,NY,11713",
    "545 Post Ave,Bellport,NY,11713",
    "48 Country Club Rd,Bellport,NY,11713",
    "500 Atlantic Ave,Bellport,NY,11713",
    "838 Doane Ave,Bellport,NY,11713",
    "709 Michigan Ave,Bellport,NY,11713",
    "101 Country Club Rd,Bellport,NY,11713",
]

loccords = []

cordsloc = [(40.718011950000005, -73.26541037906335), (40.729046600000004, -73.26574935240217), (40.710607350000004, -73.25571268918466), (40.726126, -73.271102), (40.728589150000005, -73.26380873987014), (40.7229405, -73.26129), (40.7223059, -73.26194125), (40.72966065, -73.26293818868422), (40.71258755, -73.25944937257), (40.7614646, -73.21283227433871), (40.757820550000005, -73.2120057071021), (40.75917915, -73.22038546306075), (40.75795325, -73.22277069989654), (40.7977566, -73.2517143263434), (40.792823, -73.24740451271778), (40.8027192, -73.25925154363799), (40.7789688, -73.27113320000001), (40.7627132, -73.24194775067659), (40.7699539, -73.1055798), (40.78015145, -73.14201292554745), (40.7699539, -73.1055798), (40.76001825, -73.10192408658578), (40.76934, -73.1120219), (40.75976970000001, -73.11561491311207), (40.7682428, -73.1066054), (40.7651931, -73.1189116), (40.760513450000005, -73.10970367220744), (40.7645203, -73.03784104577775), (40.7482212, -73.0226257), (40.737556, -73.040056), (40.7377786, -73.040194), (40.746233700000005, -73.04129991482301), (40.7505135, -73.0270514), (40.7518566, -73.0348316), (40.75564475, -73.0406457505196), (40.7482212, -73.0226257), (40.730826300000004, -73.48142646454752), (40.7527417, -73.48680300000001), (40.7658913, -73.49990306063853), (40.7594009, -73.48234591859206), (40.7379545, -73.48293000000001), (40.7411463, -73.4862126), (40.751986200000005, -73.48685298736453), (40.73467115, -73.4779522), (40.7525019, -73.48077787268099), (40.7629499, -72.95039209507163), (40.75789545, -72.93383893412073), (40.769446, -72.940307), (40.7765508, -72.944732), (40.75897325, -72.94856644243806), (40.77420681481481, -72.95139022222222), (40.78281535, -72.9489227237213), (40.7797394, -72.9460411010144), (40.7645257, -72.94861574350091)]


#for i in locations:
    #newloc = geolocator.geocode(i)
    #print((newloc.latitude, newloc.longitude))
    #loccords.append((newloc.latitude, newloc.longitude))
    #print(newloc.latitude)

def cordslist():
    for i in locations:
        newloc = geolocator.geocode(i)
        loccords.append((newloc.latitude, newloc.longitude))
    return loccords

cordslist()


for i in range(len(loccords)+1):
    print("------------------")
    print("------------------")
    dis = geopy.distance.geodesic(loccords[i], loccords[i+1]).km
    print (dis)
    print("------------------")
    print("------------------")
    print("------------------")
    print("------------------")
    print(loccords)


