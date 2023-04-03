import phonenumbers
from phonenumbers import carrier, geocoder, timezone


pnum= input("Enter mobile number with country code: ")
pnum=phonenumbers.parse(pnum)
print(pnum)
print(timezone.time_zones_for_number(pnum))
print(carrier.name_for_number(pnum,"en"))
print(geocoder.description_for_number(pnum,"en"))
print("Valid mobile number: ",phonenumbers.is_valid_number(pnum))
