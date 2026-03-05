def bubbleSort(arr):
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0
    passes_used = 0
    sorted_list = arr.copy()

    for i in range(n):
        swapped = False
        passes_used += 1
        for j in range(0, n - i - 1):
            total_comparisons += 1
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                total_swaps += 1
                swapped = True
                
        print(f"State setelah pass {passes_used}: {sorted_list}")
        
        # Early termination
        if not swapped:
            break
            
    return sorted_list, total_comparisons, total_swaps, passes_used

# --- Pengujian ---
print("\nSoal 2:")
print("Test Input 1: [5, 1, 4, 2, 8]")
res1 = bubbleSort([5, 1, 4, 2, 8])
print(f"Hasil: {res1}\n")

print("Test Input 2: [1, 2, 3, 4, 5]")
res2 = bubbleSort([1, 2, 3, 4, 5])
print(f"Hasil: {res2}")