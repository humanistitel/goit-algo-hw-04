import timeit
import random


# ── Merge Sort ────────────────────────────────────────────────────────────────

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ── Insertion Sort ────────────────────────────────────────────────────────────

def insertion_sort(arr: list) -> list:
    arr = arr[:]  # work on a copy
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ── Benchmark ─────────────────────────────────────────────────────────────────

def benchmark(sizes: list[int], repeats: int = 5) -> None:
    print(f"{'Size':>10} | {'Merge Sort (s)':>16} | {'Insertion Sort (s)':>20} | {'Timsort (s)':>13}")
    print("-" * 70)

    for size in sizes:
        data = [random.randint(0, size * 10) for _ in range(size)]

        merge_time = timeit.timeit(
            lambda: merge_sort(data),
            number=repeats,
        ) / repeats

        insertion_time = timeit.timeit(
            lambda: insertion_sort(data),
            number=repeats,
        ) / repeats

        timsort_time = timeit.timeit(
            lambda: sorted(data),
            number=repeats,
        ) / repeats

        print(
            f"{size:>10} | {merge_time:>16.6f} | {insertion_time:>20.6f} | {timsort_time:>13.6f}"
        )


if __name__ == "__main__":
    random.seed(42)
    sizes = [100, 1_000, 5_000, 10_000]
    print("Sorting algorithm comparison (average time per run)\n")
    benchmark(sizes)
    print(
        "\nConclusion: Timsort (Python built-in sorted/list.sort) is significantly faster"
        " than both pure-Python merge sort and insertion sort across all dataset sizes."
        " Insertion sort degrades to O(n²) for large inputs, while merge sort is O(n log n)"
        " but carries Python-level overhead (recursion + list allocation)."
        " Timsort, implemented in C and combining merge sort with insertion sort,"
        " runs in O(n log n) worst-case with highly optimised constant factors,"
        " making it the best practical choice."
    )
