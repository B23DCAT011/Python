import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    MAX_VAL = 1000000

    is_prime = [True] * (MAX_VAL + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(MAX_VAL ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_VAL + 1, i):
                is_prime[j] = False

    ans = [0] * (MAX_VAL + 1)
    for p in range(2, MAX_VAL - 5):
        if is_prime[p] and is_prime[p + 6]:
            if is_prime[p + 2] or is_prime[p + 4]:
                ans[p + 6] = 1

    for i in range(1, MAX_VAL + 1):
        ans[i] += ans[i - 1]

    T = int(input_data[0])
    out = []
    for i in range(1, T + 1):
        if i < len(input_data):
            N = int(input_data[i])
            if N > MAX_VAL:
                N = MAX_VAL

            if N > 0:
                out.append(str(ans[N - 1]))
            else:
                out.append("0")

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == '__main__':
    main()