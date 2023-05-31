import unittest
from unittest import TestCase

from src.second_question.classes.bank_delivery_optimizer import BankDeliveryOptimizer


class TestBankDeliveryOptimizerSorted(TestCase):
    """
    Classe de teste para a função BankDeliveryOptimizer.calculate_minimal_trips_with_sorted.
    """

    def test_single_trip_enough(self):
        # Caso de teste 1: Duas viagens são suficientes para atender todas as requisições.
        requests = [100, 200, 150, 300]
        max_value_per_trip = 500
        expected_trips = 2

        result = BankDeliveryOptimizer.calculate_minimal_trips_with_sorted(requests, max_value_per_trip)
        self.assertEqual(expected_trips, result)

    def test_combine_multiple_requests(self):
        # Caso de teste 2: Tres viagens são suficientes para atender todas as requisições.
        requests = [400, 100, 300, 200, 250]
        max_value_per_trip = 500
        expected_trips = 3

        result = BankDeliveryOptimizer.calculate_minimal_trips_with_sorted(requests, max_value_per_trip)
        self.assertEqual(expected_trips, result)

    def test_repeated_requests(self):
        # Caso de teste 3: Testa o caso em que existem requisições repetidas.
        requests = [200, 100, 200, 100, 200, 100]
        max_value_per_trip = 300
        expected_trips = 3

        result = BankDeliveryOptimizer.calculate_minimal_trips_with_sorted(requests, max_value_per_trip)
        self.assertEqual(expected_trips, result)

    def test_single_request_equals_limit(self):
        # Caso de teste 4: Testa o caso em que uma única requisição é igual ao valor máximo por viagem.
        requests = [500]
        max_value_per_trip = 500
        expected_trips = 1

        result = BankDeliveryOptimizer.calculate_minimal_trips_with_sorted(requests, max_value_per_trip)
        self.assertEqual(expected_trips, result)


if __name__ == '__main__':
    unittest.main()
