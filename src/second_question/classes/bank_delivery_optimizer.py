import heapq


class BankDeliveryOptimizer:

    @staticmethod
    def calculate_minimal_trips_with_sorted(requests, max_value_per_trip):
        """
        Calcula o número mínimo de viagens necessário para atender todas as requisições.

        :param requests: Uma lista de valores monetários requisitados pelas agências.
        :type requests: list[int]
        :param max_value_per_trip: O valor monetário máximo que pode ser transportado em uma única viagem.
        :type max_value_per_trip: int
        :return: O número mínimo de viagens necessário para atender todas as requisições.
        :rtype: int
        """
        sorted_requests = sorted(requests)
        total_trips = 0

        while len(sorted_requests) > 0:
            if len(sorted_requests) <= 2 and sum(sorted_requests) <= max_value_per_trip:
                total_trips += 1
                break

            first_request = sorted_requests[0]
            second_request = sorted_requests[1]
            last_request = sorted_requests[-1]

            if first_request + last_request <= max_value_per_trip:
                sorted_requests.pop()
                sorted_requests.pop(0)
                total_trips += 1

            elif first_request + second_request <= max_value_per_trip:
                sorted_requests.pop()
                if requests:
                    sorted_requests.pop(1)
                if requests:
                    sorted_requests.pop(0)
                total_trips += 2

            else:
                sorted_requests.pop()
                if len(sorted_requests) > 1:
                    sorted_requests.pop(1)
                if sorted_requests:
                    sorted_requests.pop(0)
                total_trips += 3

        return total_trips

    @staticmethod
    def calculate_minimal_trips_with_heapq(requests, max_value_per_trip):
        """
        Calcula o número mínimo de viagens necessário para atender todas as requisições.

        :param requests: Uma lista de valores monetários requisitados pelas agências.
        :type requests: list[int]
        :param max_value_per_trip: O valor monetário máximo que pode ser transportado em uma única viagem.
        :type max_value_per_trip: int
        :return: O número mínimo de viagens necessário para atender todas as requisições.
        :rtype: int
        """
        heapq.heapify(requests)

        total_trips = 0

        while len(requests) > 0:
            if len(requests) <= 2 and sum(requests) <= max_value_per_trip:
                total_trips += 1
                break

            first_request = requests[0]
            second_request = requests[1]
            last_request = requests[-1]

            if first_request + last_request <= max_value_per_trip:
                requests.pop()
                heapq.heappop(requests)
                total_trips += 1

            elif first_request + second_request <= max_value_per_trip:
                requests.pop()
                if requests:
                    heapq.heappop(requests)
                if requests:
                    heapq.heappop(requests)
                total_trips += 2

            else:
                requests.pop()
                if requests:
                    heapq.heappop(requests)
                if requests:
                    heapq.heappop(requests)
                total_trips += 3

        return total_trips
