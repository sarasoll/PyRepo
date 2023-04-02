
import phonenumbers
from phonenumbers import carrier

phone_number = phonenumbers.parse("+966570409960")
print(carrier.name_for_number(phone_number, "en"))