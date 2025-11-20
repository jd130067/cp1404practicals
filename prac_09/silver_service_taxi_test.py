"""
Basic testing for silver service taxi class.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

normal_taxi = Taxi("Yellow", 100)
fanci_taxi = SilverServiceTaxi("Silver", 100, 2)
normal_taxi.drive(53)
fanci_taxi.drive(53)

print(normal_taxi)
print(fanci_taxi)

print(f"Normal Cost: {normal_taxi.get_fare()}")
print(f"Fancy Cost: {fanci_taxi.get_fare()}")

