def z_arr(s):
    Z = [0] * len(s)
    Z[0] = 0
    rt = 0
    lt = 0
    for k in range(1, len(s)):
        if k > rt:
            n = 0
            while n + k < len(s) and s[n] == s[n + k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k + n - 1
        else:
            p = k - lt  # Pair index.
            right_part_len = rt - k + 1

            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                lt = k
                rt = i - 1
    return Z


s = input()
print(*z_arr(s))
