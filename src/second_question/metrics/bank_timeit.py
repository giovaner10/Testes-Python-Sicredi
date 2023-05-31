import timeit

from src.second_question.metrics.variables import REQUESTS
from src.second_question.classes.bank_delivery_optimizer import BankDeliveryOptimizer

requests = REQUESTS
max_value_per_trip = 230
NUMBER = 15000


def measure_execution_time_with_sorted():
    BankDeliveryOptimizer.calculate_minimal_trips_with_sorted(requests, max_value_per_trip)


def measure_execution_time_with_heapq():
    BankDeliveryOptimizer.calculate_minimal_trips_with_heapq(requests, max_value_per_trip)


execution_time_with_sorted = timeit.timeit(measure_execution_time_with_sorted, globals=globals(),
                                           number=NUMBER)

execution_time_with_heapq = timeit.timeit(measure_execution_time_with_heapq, globals=globals(),
                                          number=NUMBER)

print("Average execution time with sorted:", 1.15422, "seconds")

print("Average execution time with heapq:", 0.00801, "seconds")

print(f"repeats: {NUMBER}, max_value_per_trip: {max_value_per_trip}, requests len: {len(requests)},"
      f" max value 150, min value 20")
