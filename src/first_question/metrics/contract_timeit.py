import timeit

from src.first_question.classes.contract_manager import ContractManager
from src.first_question.metrics.variables import OPEN_CONTRACTS, renegotiated_contracts, top_n_contracts_by_value

open_contracts = OPEN_CONTRACTS
renegotiated_contracts = renegotiated_contracts
top_n = 60
NUMBER = 10000


def measure_execution_time_with_sorted():
    ContractManager.get_top_n_open_contracts_with_sorted(OPEN_CONTRACTS, renegotiated_contracts,
                                                         top_n_contracts_by_value)


def measure_execution_time_with_quick_sort():
    ContractManager.get_top_n_open_contracts_with_quick_sort(OPEN_CONTRACTS, renegotiated_contracts,
                                                             top_n_contracts_by_value)


def measure_execution_time_with_heapq_nlargest():
    ContractManager.get_top_n_open_contracts_with_heapq(OPEN_CONTRACTS, renegotiated_contracts,
                                                        top_n_contracts_by_value)


execution_time_with_sorted = timeit.timeit(measure_execution_time_with_sorted, globals=globals(),
                                           number=NUMBER)

execution_time_with_quick_sort = timeit.timeit(measure_execution_time_with_quick_sort, globals=globals(),
                                               number=NUMBER)

execution_time_with_heapq_nlargest = timeit.timeit(measure_execution_time_with_heapq_nlargest, globals=globals(),
                                                   number=NUMBER)


print("Average execution time with sorted:", execution_time_with_sorted, "seconds")

print("Average execution time with quick sort:", execution_time_with_quick_sort, "seconds")

print("Average execution time with heapq largest:", execution_time_with_heapq_nlargest, "seconds")

print(f"repeats: {NUMBER}, renegotiated_contracts: {len(renegotiated_contracts)}, top_n: {top_n}")
