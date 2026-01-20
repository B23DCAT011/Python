def count_triplets_optimized(arr, n):
    if n < 3:
        return 0
    arr.sort()
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                count += 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return count


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    result = count_triplets_optimized(arr, n)
    print(result)