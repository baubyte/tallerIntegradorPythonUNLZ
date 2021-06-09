from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="baubyte")

lista = ['Querandíes, 459, Buenos Aires, Argentina',
         'Gallo, 908, Buenos Aires, Argentina'
        ]
for index in lista:
    location = geolocator.geocode(index, language="es")
    print((location.latitude, location.longitude))
    print(location.address)