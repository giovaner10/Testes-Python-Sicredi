import heapq
import random

from src.first_question.classes.contract import Contract


class ContractManager:

    @staticmethod
    def get_top_n_open_contracts_with_sorted(open_contracts, renegotiated_contracts, top_n_contracts_by_value):
        """
        Retorna uma lista de identificadores dos N principais devedores que não renegociaram suas dívidas.

        :param open_contracts: Uma lista de contratos abertos.
        :type open_contracts: list[Contract]
        :param renegotiated_contracts: Uma lista de identificadores dos contratos renegociados.
        :type renegotiated_contracts: list[int]
        :param top_n_contracts_by_value: O número de principais devedores a serem retornados.
        :type top_n_contracts_by_value: int
        :return: Uma lista contendo os identificadores dos N principais devedores em ordem decrescente.
        :rtype: list[int]
        """
        filtered_contracts = [
            contract for contract in open_contracts
            if contract.identifier not in renegotiated_contracts
        ]

        sorted_contracts = sorted(filtered_contracts, key=lambda contract: contract.debt, reverse=True)

        debtors_top_n = [contract.identifier for contract in sorted_contracts[:top_n_contracts_by_value]]

        return debtors_top_n

    @staticmethod
    def get_top_n_open_contracts_with_quick_sort(open_contracts, renegotiated_contracts, top_n_contracts_by_value):
        """
        Retorna uma lista dos N maiores devedores que ainda não renegociaram seus débitos.

        Args:
            open_contracts (list): Uma lista contendo instâncias de objetos Contract representando contratos em aberto.
            renegotiated_contracts (list): Uma lista de identificadores de contratos que já foram renegociados.
            top_n_contracts_by_value (int): O número de maiores devedores a serem retornados.

        Returns:
            list: Uma lista contendo os identificadores dos N maiores devedores em ordem decrescente de dívida.

        Raises:
            None

        """

        filtered_contracts = [
            contract for contract in open_contracts
            if contract.identifier not in renegotiated_contracts
        ]

        def quick_select(arr, left, right, k):
            """
            Implementação do algoritmo QuickSelect para encontrar o k-ésimo maior elemento em um array.

            Args:
                arr (list): O array a ser particionado.
                left (int): O índice esquerdo do array.
                right (int): O índice direito do array.
                k (int): A posição do elemento desejado no array.

            Returns:
                object: O k-ésimo maior elemento do array.

            """
            while True:
                if left == right:
                    return arr[left]

                pivot_index = random.randint(left, right)
                pivot_index = partition(arr, left, right, pivot_index)

                if k == pivot_index:
                    return arr[k]
                elif k < pivot_index:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1

        def partition(arr, left, right, pivot_index):
            """
            Particiona o array em torno de um pivô e retorna a posição final do pivô.

            Args:
                arr (list): O array a ser particionado.
                left (int): O índice esquerdo do array.
                right (int): O índice direito do array.
                pivot_index (int): O índice do pivô.

            Returns:
                int: A posição final do pivô após a partição.

            """
            pivot_value = arr[pivot_index].debt
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            store_index = left

            for i in range(left, right):
                if arr[i].debt > pivot_value:
                    arr[i], arr[store_index] = arr[store_index], arr[i]
                    store_index += 1

            arr[right], arr[store_index] = arr[store_index], arr[right]
            return store_index

        if top_n_contracts_by_value <= 0 or top_n_contracts_by_value > len(filtered_contracts):
            return []

        top_debts = [
            quick_select(filtered_contracts, 0, len(filtered_contracts) - 1, i)
            for i in range(top_n_contracts_by_value)
        ]
        debtors_top_n = [contract.identifier for contract in top_debts]

        return debtors_top_n

    @staticmethod
    def get_top_n_open_contracts_with_heapq(open_contracts, renegotiated_contracts, top_n_contracts_by_value):
        """
        Retorna uma lista de identificadores dos top N devedores que não renegociaram suas dívidas.

        :param open_contracts: Uma lista de contratos em aberto.
        :type open_contracts: list[Contract]
        :param renegotiated_contracts: Uma lista de identificadores de contratos renegociados.
        :type renegotiated_contracts: list[int]
        :param top_n_contracts_by_value: O número de principais devedores a serem retornados.
        :type top_n_contracts_by_value: int
        :return: Uma lista contendo os identificadores dos top N devedores em ordem decrescente.
        :rtype: list[int]
        """
        renegotiated_set = set(renegotiated_contracts)
        filtered_contracts = [
            contract for contract in open_contracts
            if contract.identifier not in renegotiated_set
        ]

        top_n_contracts = heapq.nlargest(top_n_contracts_by_value, filtered_contracts, key=lambda contract: contract.debt)

        debtors_top_n = [contract.identifier for contract in top_n_contracts]

        return debtors_top_n
