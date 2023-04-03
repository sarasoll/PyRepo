
import phonenumbers
from phonenumbers import timezone

pnum = phonenumbers.parse("+966570409960")
print(timezone.time_zones_for_number(pnum))
