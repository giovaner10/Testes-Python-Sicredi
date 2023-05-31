import unittest
from unittest import TestCase

from src.first_question.classes.contract import Contract
from src.first_question.classes.contract_manager import ContractManager


class TestContractHeapq(TestCase):
    """
    Classe de teste para a função get_top_n_open_contracts_with_heapq_nlargest.
    """
    def test_get_top_n_open_contracts_with_heapq_nlargest(self):
        # Caso de teste 1: Contratos em aberto, alguns renegociados
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300),
            Contract(4, 400),
            Contract(5, 500)
        ]
        renegotiated = [3, 5]
        top_n_contracts_by_value = 3

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = [4, 2, 1]
        self.assertEqual(result, expected_result)

    def test_get_top_n_open_contracts_all_renegotiated_with_heapq_nlargest(self):
        # Caso de teste 2: Todos os contratos em aberto já renegociados
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300)
        ]
        renegotiated = [1, 2, 3]
        top_n_contracts_by_value = 2

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = []
        self.assertEqual(result, expected_result)

    def test_get_top_n_open_contracts_more_contracts_than_top_n_with_heapq_nlargest(self):
        # Caso de teste 3: Mais contratos em aberto do que a quantidade desejada de maiores devedores
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300),
            Contract(4, 400),
            Contract(5, 500)
        ]
        renegotiated = []
        top_n_contracts_by_value = 2

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = [5, 4]
        self.assertEqual(result, expected_result)

    def test_get_top_n_open_contracts_empty_contracts_list_with_heapq_nlargest(self):
        # Caso de teste 4: Lista de contratos em aberto vazia
        contracts = []
        renegotiated = [1, 2, 3]
        top_n_contracts_by_value = 3

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = []
        self.assertEqual(result, expected_result)

    def test_get_top_n_open_contracts_empty_renegotiated_list_with_heapq_nlargest(self):
        # Caso de teste 5: Lista de contratos renegociados vazia
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300)
        ]
        renegotiated = []
        top_n_contracts_by_value = 2

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = [3, 2]
        self.assertEqual(result, expected_result)

    def test_get_top_n_open_contracts_zero_top_n_with_heapq_nlargest(self):
        # Caso de teste 6: Valor zero para a quantidade desejada de maiores devedores
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300)
        ]
        renegotiated = []
        top_n_contracts_by_value = 0

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = []
        self.assertEqual(result, expected_result)

    def test_get_top_n_open_contracts_equal_values_with_heapq_nlargest(self):
        # Caso de teste 7: Valores iguais para os contratos em aberto
        contracts = [
            Contract(1, 200),
            Contract(2, 200),
            Contract(3, 200),
            Contract(4, 200),
            Contract(5, 200)
        ]
        renegotiated = []
        top_n_contracts_by_value = 3

        result = ContractManager.get_top_n_open_contracts_with_heapq(contracts, renegotiated,
                                                                     top_n_contracts_by_value)

        expected_result = [1, 2, 3]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
