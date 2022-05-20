
# O(n!)...
# def permutation_sort(A):
#     for B in permutations(A):
#         if is_sorted(B):
#             return B

def binary_search(sorted_list: list, target, low=None, high=None):
    low, high = low or 0, high or len(sorted_list) - 1
    if low > high:
        return -1
    mid = (high + low) // 2
    if target == sorted_list[mid]:
        return mid
    elif target > sorted_list[mid]:
        return binary_search(sorted_list, target, mid + 1, high)
    elif target < sorted_list[mid]:
        return binary_search(sorted_list, target, low, mid)

def prefix_max(iterable, idx):
    # Return max of iterable between index 0:i
    if idx > 0:
        j = prefix_max(iterable, idx - 1)
        if iterable[idx] < iterable[j]:
            return j
    return idx

def selection_sort(iterable, max_idx = None) -> None:
    # O(N^2), In place sort
    if max_idx is None: max_idx = len(iterable) - 1
    if max_idx > 0:
        max_val_idx = prefix_max(iterable, max_idx)
        iterable[max_idx], iterable[max_val_idx] = iterable[max_val_idx], iterable[max_idx]
        selection_sort(iterable, max_idx - 1)

def merge(l_iterable, r_iterable, final_iterable, i, j, left, right):
    if left < right:
        if (j <= 0) or (i > 0 and l_iterable[i - 1] > r_iterable[j - 1]):
            final_iterable[right - 1] = l_iterable[i - 1]
            i = i - 1
        else:
            final_iterable[right - 1] = r_iterable[j - 1]
            j = j - 1
        merge(l_iterable, r_iterable, final_iterable, i, j, left, right - 1)

def merge_sort(iterable, left = 0, right = None) -> None:
    '''Sort iterable[left:right]'''
    if right == None: right = len(iterable)
    if 1 < right - left:
        mid = (left + right + 1) // 2
        merge_sort(iterable, left, mid)
        merge_sort(iterable, mid, right)
        L, R = iterable[left:mid], iterable[mid:right]
        merge(L, R, iterable, len(L), len(R), left, right)


def main():
    some_list = [1,2,5,37,3457,23,52345,7235,6,247,134,6,234,13245,234,56,234,5,342,67247645,6,23,45,1,367,12,7,3,7,2534,76,26,3,245,23,4,27,35,7,4238,5,37324,2,24,56,42,234,5,1257,24,72,356,32,5,134,6,325,72,457,3,56,2345]
    print(some_list)
    # print(binary_search(some_list,1))
    # print(prefix_max(some_list,9))
    # selection_sort(some_list)
    merge_sort(some_list)
    print(some_list)

if __name__=="__main__":
    main()