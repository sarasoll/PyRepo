
import phonenumbers
from phonenumbers import timezone

phone_number = phonenumbers.parse("+966570409960")
print(timezone.time_zones_for_number(phone_number))