import random
import timeit

def merge_sort(arr):
    """Сортування злиттям Merge Sort"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    """Сортування вставками Insertion Sort"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def test_sorting(sort_function, arr):
    """
    Тестування алгоритму сортування на наборах даних різного розміру. Timsort
    """
    time_taken = timeit.timeit(lambda: sort_function(arr.copy()), number=10)
    return time_taken

if __name__ == "__main__":
    print("Тестування алгоритмів сортування:")
    # Розміри наборів даних для тестування
    array_sizes = [10, 100, 1000, 10000]

    for arr_size in array_sizes:
        # Генерація випадкових списків
        test_data = [random.randint(0, 10000) for _ in range(arr_size)]
        test_data_copy1 = test_data.copy()
        test_data_copy2 = test_data.copy()
        test_data_copy3 = test_data.copy()

        print(f"Розмір массива: {arr_size}")
        print(f"Merge Sort: {test_sorting(merge_sort, test_data_copy1):.6f} сек")
        print(f"Insertion Sort: {test_sorting(insertion_sort, test_data_copy2):.6f} сек")
        print(f"Timsort (sorted): {test_sorting(sorted, test_data_copy3):.6f} сек")
        print()

    print("Висновок:")
    print("Timsort (вбудована функція sorted) працює значно швидше, ніж сортування злиттям та сортування вставками, особливо для великих наборів даних. Це пов'язано з тим, що Timsort - це гібридний алгоритм, який поєднує в собі переваги сортування злиттям та сортування вставками.")
    print("У більшості випадків, використання вбудованих алгоритмів сортування, як Timsort, більш ефективне, ніж реалізація власних алгоритмів з нуля.")
