import time
import random
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    # cópia para não alterar o vetor original dos outros testes
    arr_copy = arr.copy()
    swaps = 0

    for i in range(n):
        # se nenhuma troca ocorrer, o vetor já está ordenado
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return arr_copy, swaps

def merge_sort(arr):
    arr_copy = arr.copy()

    def _merge_sort_recursive(sub_arr):
        moves = 0
        if len(sub_arr) > 1:
            mid = len(sub_arr) // 2
            L = sub_arr[:mid]
            R = sub_arr[mid:]

            # conta as movimentações ao dividir/copiar para os arrays auxiliares
            moves += len(L) + len(R)

            moves += _merge_sort_recursive(L)
            moves += _merge_sort_recursive(R)

            i = j = k = 0

            # Intercalação (Merge)
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    sub_arr[k] = L[i]
                    i += 1
                else:
                    sub_arr[k] = R[j]
                    j += 1
                k += 1
                moves += 1  # Movimentação ao escrever no vetor principal

            while i < len(L):
                sub_arr[k] = L[i]
                i += 1
                k += 1
                moves += 1

            while j < len(R):
                sub_arr[k] = R[j]
                j += 1
                k += 1
                moves += 1

        return moves

    total_moves = _merge_sort_recursive(arr_copy)
    return arr_copy, total_moves


def quick_sort(arr):
    arr_copy = arr.copy()
    total_swaps = 0

    def partition(low, high):
        nonlocal total_swaps
        pivot = arr_copy[high]
        i = low - 1

        for j in range(low, high):
            if arr_copy[j] <= pivot:
                i += 1
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
                total_swaps += 1

        arr_copy[i + 1], arr_copy[high] = arr_copy[high], arr_copy[i + 1]
        total_swaps += 1
        return i + 1

    def _quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort_recursive(low, pi - 1)
            _quick_sort_recursive(pi + 1, high)

    _quick_sort_recursive(0, len(arr_copy) - 1)
    return arr_copy, total_swaps

# tamanhos dos vetores
tamanhos = [1000, 10000, 100000]
algoritmos = {
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

for n in tamanhos:
    print(f"\n--- Gerando vetor aleatório de tamanho: {n} ---")
    # vetor original
    vetor_original = [random.randint(0, 1000000) for _ in range(n)]

    for nome, func in algoritmos.items():
        # se o buble sort demorou demais no anterior pula o de 100k
        if nome == "Bubble Sort" and n == 100000:
            print(f"{nome} para {n} elementos: Provavelmente excederá 5 minutos. Interrompa se necessário.")

        tempos = []
        operacoes = 0

        for i in range(3):
            start_time = time.time()
            vetor_ordenado, ops = func(vetor_original)
            end_time = time.time()

            duracao = end_time - start_time
            tempos.append(duracao)
            operacoes = ops

        tempo_medio = np.mean(tempos)
        desvio_padrao = np.std(tempos)

        print(f"\nAlgoritmo: {nome}")
        print(f"  Execução 1: {tempos[0]:.6f} s")
        print(f"  Execução 2: {tempos[1]:.6f} s")
        print(f"  Execução 3: {tempos[2]:.6f} s")
        print(f"  Tempo Médio: {tempo_medio:.6f} s")
        print(f"  Desvio Padrão: {desvio_padrao:.6f} s")
        print(f"  Trocas/Movimentações: {operacoes}")