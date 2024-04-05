import tkinter as tk
import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_display(arr, i, min_idx)
        time.sleep(0.1)
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_display(arr, j, j+1)
                time.sleep(0.1)
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        update_display(arr, j+1, i)
        time.sleep(0.1)
    return arr

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

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot_idx = partition(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)
        update_display(arr)  # Mise à jour de l'affichage après chaque partition
        time.sleep(0.1)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

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
        update_display(arr)  # Mise à jour de l'affichage après chaque échange
        time.sleep(0.1)

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
                update_display(arr, i, i+gap)  # Ajout de la mise à jour de l'affichage
                time.sleep(0.1)
                swapped = True

    return arr


def update_display(arr, idx1=-1, idx2=-1):
    canvas.delete("all")
    for i, val in enumerate(arr):
        color = "blue"
        if i == idx1 or i == idx2:
            color = "red"
        canvas.create_rectangle(i * 20, 100 - val * 10, (i + 1) * 20, 100, fill=color)
        canvas.create_text((i * 20) + 10, 105 - val * 10, text=str(val))


def sort_array(sort_function):
    global arr
    if sort_function == quick_sort or sort_function == heap_sort:
        sort_function(arr)
    else:
        arr = sort_function(arr)
        update_display(arr)


def generate_array():
    global arr
    arr = [random.randint(1, 10) for _ in range(10)]
    update_display(arr)


root = tk.Tk()
root.title("Visualisation des algorithmes de tri")

canvas = tk.Canvas(root, width=200, height=110, bg="white")
canvas.pack()

sort_functions = {
    "Tri par sélection": selection_sort,
    "Tri à bulles": bubble_sort,
    "Tri par insertion": insertion_sort,
    "Tri fusion": merge_sort,
    "Tri rapide": quick_sort,
    "Tri par tas": heap_sort,
    "Tri à peigne": comb_sort
}

for name, func in sort_functions.items():
    tk.Button(root, text=name, command=lambda f=func: sort_array(f)).pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(root, text="Générer", command=generate_array)
generate_button.pack(side=tk.LEFT, padx=10)

arr = [random.randint(1, 10) for _ in range(10)]
update_display(arr)

root.mainloop()
