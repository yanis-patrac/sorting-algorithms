from sorting import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort, comb_sort

def main():
    arr = [5, 2, 9, 1, 5, 6]
    
    print("Original array:", arr)

    sorted_arr_selection = selection_sort(arr.copy())
    print("Selection Sort:", sorted_arr_selection)

    sorted_arr_bubble = bubble_sort(arr.copy())
    print("Bubble Sort:", sorted_arr_bubble)

    sorted_arr_insertion = insertion_sort(arr.copy())
    print("Insertion Sort:", sorted_arr_insertion)

    sorted_arr_merge = merge_sort(arr.copy())
    print("Merge Sort:", sorted_arr_merge)

    sorted_arr_quick = quick_sort(arr.copy())
    print("Quick Sort:", sorted_arr_quick)

    sorted_arr_heap = heap_sort(arr.copy())
    print("Heap Sort:", sorted_arr_heap)

    sorted_arr_comb = comb_sort(arr.copy())
    print("Comb Sort:", sorted_arr_comb)

if __name__ == "__main__":
    main()
