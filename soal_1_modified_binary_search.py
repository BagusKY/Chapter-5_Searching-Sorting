def countOccurrences(sortedList, target):
    def findBound(arr, target, isFirst):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                result = mid
                if isFirst:
                    right = mid - 1  # Lanjut cari ke kiri
                else:
                    left = mid + 1   # Lanjut cari ke kanan
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first_idx = findBound(sortedList, target, True)
    if first_idx == -1:
        return 0  # Elemen tidak ditemukan
    
    last_idx = findBound(sortedList, target, False)
    return last_idx - first_idx + 1

# --- Pengujian ---
print("Soal 1:")
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 4)) # Output: 4
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 5)) # Output: 0