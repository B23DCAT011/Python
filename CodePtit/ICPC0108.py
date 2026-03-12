import sys


def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield int(word)

    input_gen = get_input()

    try:
        t_str = next(input_gen)
    except StopIteration:
        return

    t = int(t_str)

    for _ in range(t):
        try:
            n = int(next(input_gen))

            a = []
            for i in range(n):
                a.append(int(next(input_gen)))

            a.sort()
            count = 0

            for i in range(n - 2):
                left = i + 1
                right = n - 1

                target = -a[i]

                while left < right:
                    current_sum = a[left] + a[right]
                    if current_sum == target:
                        count += 1

                        left += 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
            print(count)
        except StopIteration:
            break


if __name__ == "__main__":
    solve()