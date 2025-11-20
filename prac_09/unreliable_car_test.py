"""
Tests for unreliable car class.
"""

from prac_09.unreliable_car import UnreliableCar

NUMBER_OF_TESTS = 1000

sketch_car = UnreliableCar("ricky", 100000, 99)

successes = 0
failure = 0

for i in range(NUMBER_OF_TESTS):
    if sketch_car.drive(1):
        successes += 1
    else:
        failure += 1

print(f" Drove: {successes}")
print(f"Didn't drive: {failure}")

estimated_reliability = successes/failure
print(estimated_reliability)
