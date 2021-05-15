import random
from typing import Final, List

def quick_sort(a: List[int]):
    if len(a) <= 1:
        return a

    left: List[int] = list()
    right: List[int] = list()
    num_pivot: int = 0

    pivot: Final[int] = random.choice(a)

    for ai in a:
        if ai < pivot:
            left.append(ai)
        elif ai > pivot:
            right.append(ai)
        else:
            num_pivot += 1

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] * num_pivot + right


if __name__ == "__main__":
    a = [34, 2, -1, 0, 400, 58, -3]
    print(a)
    print(quick_sort(a))