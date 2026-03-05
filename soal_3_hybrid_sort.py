import random

def insertionSortOps(arr):
    comparisons, swaps = 0, 0
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j+1] = a[j]
                swaps += 1
                j -= 1
            else:
                break
        a[j+1] = key
    return comparisons + swaps

def selectionSortOps(arr):
    comparisons, swaps = 0, 0
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return comparisons + swaps

def hybridSort(theSeq, threshold=10):
    if len(theSeq) <= threshold:
        return insertionSortOps(theSeq)
    else:
        return selectionSortOps(theSeq)

# --- Pengujian dan Tabel ---
print("\nSoal 3 (Hasil Evaluasi):")
print(f"{'Size':<10} | {'Pure Insertion':<18} | {'Pure Selection':<18} | {'Hybrid Sort'}")
print("-" * 65)

sizes = [50, 100, 500]
for size in sizes:
    test_arr = [random.randint(1, 1000) for _ in range(size)]
    ins_ops = insertionSortOps(test_arr)
    sel_ops = selectionSortOps(test_arr)
    hyb_ops = hybridSort(test_arr)
    print(f"{size:<10} | {ins_ops:<18} | {sel_ops:<18} | {hyb_ops}")