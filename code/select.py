selectsort = (
    lambda l: [] if not l else (
        lambda idx, v: [v] + selectsort(l[:idx] + l[idx + 1:]))(
            *min(enumerate(l), key=lambda t: t[1])
    )
)

print(selectsort([1, 2, 3, 22, 4, -1]))
