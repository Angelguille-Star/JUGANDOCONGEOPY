from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Mike")
location = geolocator.geocode("32.4999481, -116.9314954")
print(location.address)

