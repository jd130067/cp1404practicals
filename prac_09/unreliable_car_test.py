"""
Tests for unreliable car class.
"""

from prac_09.unreliable_car import UnreliableCar

NUMBER_OF_TESTS = 1000

# Not worried about testing fuel just need enough to run many tests
sketch_car = UnreliableCar("ricky", 100000, 90)

successes = 0
failure = 0

# Test 1000 times to check if the randomness is working
for i in range(NUMBER_OF_TESTS):
    if sketch_car.drive(1):
        successes += 1
    else:
        failure += 1

print(f" Drove: {successes}")
print(f"Didn't drive: {failure}")

estimated_reliability = (successes/failure) * 10  # Multiplied by 10 so it equates to the actual reliability
print(f"{estimated_reliability}")
# Tests Results (reliability set to 90):
# Expecting 100 failures, 900 successes
# 90.0, 86.15, 84.34, 74.75, 99.89
# About correct
