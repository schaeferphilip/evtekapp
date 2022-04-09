from flask import Flask
import folium
from geopy.geocoders import Nominatim
import geopy
import geopy.distance
from geopy import distance

import numpy as np
from sklearn.neighbors import NearestNeighbors
import networkx as nx

import warnings
warnings.filterwarnings('ignore') 

app = Flask(__name__)

geolocator = Nominatim(user_agent="my_user_agent")

totaldistance = 0
totaltime = 0
distime = ""

start = "1560 5th Ave,Bay Shore,NY,11706"
startcords = (40.753783, -73.264506)

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


@app.route('/map', methods=['GET'])
def base():
    global totaldistance
    global totaltime
    global distime
    global startcords

    maptest = folium.Map(
        location=[40.7411463, -73.4862126]
    )

    # geocoding addresses to coordinates
    for i in locations:
        new = geolocator.geocode(i)
        folium.Marker(location = [new.latitude, new.longitude], popup=i).add_to(maptest)
        loccords.append((new.latitude, new.longitude))

    ###
    points = np.asarray(loccords)
    # find nearest neighbors
    clf = NearestNeighbors(11).fit(points)
    G = clf.kneighbors_graph()
    T = nx.from_scipy_sparse_matrix(G)
    # indexes of the new order 
    order = list(nx.dfs_preorder_nodes(T, 0))
    # sorted arrays 
    orderedpoints = points[order]
    ###
    new_points = orderedpoints.tolist()
    new_points.insert(0,startcords)
    print(new_points)

    startmarker = folium.Marker(location = [40.753783, -73.264506], popup=str("Start: "+start), icon=folium.Icon(color="green", icon="info-sign"))
    startmarker.add_to(maptest)


    

    route = folium.PolyLine(new_points, color='red')
    route.add_to(maptest)

    #calculating total distance
    for i in range(len(new_points)-1):
        totaldistance += distance.distance(new_points[i], new_points[i+1]).km

    print("Total distance in km: ")
    print(totaldistance)

    #total driving time: average speed limit long Island 55 mp/h or 88 km/h
    totaltime = totaldistance/88
    print("Total driving time in hours: ")
    print(totaltime)

    distime = str("Total distance in km: " + str(round(totaldistance, 2)) + " km, " + "Total driving time in hours: " + str(round(totaltime, 2)) + " hours")

    print(distime)

    maptest.save("Map.html")
    return maptest._repr_html_()


@app.route('/api', methods=['GET'])
def index():
    return {
        "hello": "Hello, World!",
        "test": "Test",
        "success": "Connection to Flask backend: successful!",
        "distime": distime
    } 
    



