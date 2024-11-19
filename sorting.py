# Main Program
X = [1, 5, 6, 4, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Merge Sort Execution
merge_sorted = X.copy()
merge_sort(merge_sorted)
print("Sorted using Merge Sort:", merge_sorted)

# Algoritma Merge Sort memiliki kompleksitas waktu O(n log n) untuk semua kasus 
# (best case, average case, dan worst case) karena array selalu dibagi menjadi dua bagian 
# hingga elemen tunggal dan kemudian digabung kembali secara terurut. Algoritma ini stabil, 
# karena elemen dengan nilai yang sama akan tetap mempertahankan urutannya seperti dalam array asli. 
# Merge Sort cocok untuk dataset besar karena efisiensinya yang konsisten, namun memerlukan ruang tambahan O(n) untuk array sementara 
# selama proses penggabungan, sehingga kurang ideal untuk sistem dengan keterbatasan memori.


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Quick Sort Execution
quick_sorted = quick_sort(X)
print("Sorted using Quick Sort:", quick_sorted)

# Algoritma Quick Sort memiliki kompleksitas waktu O(n log n) pada best case dan average case ketika pivot membagi array secara proporsional. 
# Namun, pada worst case, kompleksitasnya menjadi O(n²), yaitu ketika pivot selalu memilih elemen terkecil atau terbesar, 
# seperti pada array yang sudah terurut. Algoritma ini tidak memerlukan banyak ruang tambahan, 
# sehingga lebih efisien dibandingkan Merge Sort dalam hal penggunaan memori. Namun, Quick Sort bersifat tidak stabil, 
# sehingga elemen dengan nilai yang sama bisa berubah urutannya. Pemilihan pivot yang baik sangat penting untuk 
# menghindari kinerja buruk pada worst case.







