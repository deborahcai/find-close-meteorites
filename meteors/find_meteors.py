import math
import requests

# https://en.wikipedia.org/wiki/Haversine_formula
def calc_dist(lat1, lon1, lat2, lon2):
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)

	h = math.sin( (lat2 - lat1) / 2) ** 2 + \
		math.cos(lat1) * \
		math.cos(lat2) * \
		math.sin( (lon2 - lon1) / 2 ) ** 2

	return 6372.8 * 2 * math.asin(math.sqrt(h))
	
# sort dictionary
def get_dist(meteor):
	return meteor.get('distance', math.inf)


my_loc = (1.440324, 103.784541)

meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
meteor_data = meteor_resp.json()

for meteor in meteor_data:
	# if 'reclat' not in meteor or 'reclong' not in meteor: continue
	if not ('reclat' in meteor and 'reclong' in meteor): continue
	meteor['distance'] = calc_dist(float(meteor['reclat']), 
									float(meteor['reclong']), 
										my_loc[0], 
										my_loc[1])

# pass the function as parameter
meteor_data.sort(key=get_dist)

print(meteor_data[0:10])