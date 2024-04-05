import time
import random

# Tri par sélection
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Tri à bulles
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Tri par insertion
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Tri fusion
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Tri rapide
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Tri par tas
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# Tri à peigne
def comb_sort(arr):
    def get_next_gap(gap):
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return int(gap)

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr

# Générer une liste aléatoire de taille n
n = 1000
liste = [random.random() for _ in range(n)]

# Mesurer le temps d'exécution de chaque algorithme de tri
debut = time.time()
selection_sort(liste.copy())
fin = time.time()
temps_execution_selection = fin - debut
print("Temps d'exécution du tri par sélection:", temps_execution_selection)

debut = time.time()
bubble_sort(liste.copy())
fin = time.time()
temps_execution_bulles = fin - debut
print("Temps d'exécution du tri à bulles:", temps_execution_bulles)

debut = time.time()
insertion_sort(liste.copy())
fin = time.time()
temps_execution_insertion = fin - debut
print("Temps d'exécution du tri par insertion:", temps_execution_insertion)

debut = time.time()
merge_sort(liste.copy())
fin = time.time()
temps_execution_fusion = fin - debut
print("Temps d'exécution du tri fusion:", temps_execution_fusion)

debut = time.time()
quick_sort(liste.copy())
fin = time.time()
temps_execution_rapide = fin - debut
print("Temps d'exécution du tri rapide:", temps_execution_rapide)

debut = time.time()
heap_sort(liste.copy())
fin = time.time()
temps_execution_tas = fin - debut
print("Temps d'exécution du tri par tas:", temps_execution_tas)

debut = time.time()
comb_sort(liste.copy())
fin = time.time()
temps_execution_comb = fin - debut
print("Temps d'exécution du tri à peigne:", temps_execution_comb)
