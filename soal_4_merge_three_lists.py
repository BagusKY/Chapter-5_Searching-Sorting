def mergeThreeSortedLists(listA, listB, listC):
    result = []
    i, j, k = 0, 0, 0
    lenA, lenB, lenC = len(listA), len(listB), len(listC)

    while i < lenA or j < lenB or k < lenC:
        # Gunakan float('inf') jika pointer sudah mencapai akhir list
        valA = listA[i] if i < lenA else float('inf')
        valB = listB[j] if j < lenB else float('inf')
        valC = listC[k] if k < lenC else float('inf')

        # Cari nilai terkecil di antara ketiga pointer
        min_val = min(valA, valB, valC)

        if min_val == valA:
            result.append(valA)
            i += 1
        elif min_val == valB:
            result.append(valB)
            j += 1
        else:
            result.append(valC)
            k += 1

    return result

# --- Pengujian ---
print("\nSoal 4:")
print(mergeThreeSortedLists([1, 5, 9], [2, 6, 10], [3, 4, 7]))
# Output: [1, 2, 3, 4, 5, 6, 7, 9, 10]