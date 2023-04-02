import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileno = input("Enter mobile number with country code: ")
mobileno=phonenumbers.parse(mobileno)
print(mobileno)
print(timezone.time_zones_for_number(mobileno))
print(carrier.name_for_number(mobileno,"en"))
print(geocoder.description_for_number(mobileno,"en"))
print("Valid mobile number: ",phonenumbers.is_valid_number(mobileno))