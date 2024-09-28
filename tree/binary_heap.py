def max_heapify(A, i, heap_size):
    # 左の子ノードのインデックス
    left = 2 * i + 1
    # 右の子ノードのインデックス
    right = 2 * i + 2
    # 現在のノードを最大値の位置と仮定
    largest = i

    # 左の子がヒープのサイズ内であり、かつ現在の最大値より大きい場合
    if left < heap_size and A[left] > A[largest]:
        largest = left

    # 右の子がヒープのサイズ内であり、かつ現在の最大値より大きい場合
    if right < heap_size and A[right] > A[largest]:
        largest = right

    # 最大値の位置が変わっている場合、入れ替えて再帰的に調整
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    # 最後の親ノードから順番に max_heapify を行う
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, i, heap_size)


# テスト用配列
A = [3, 5, 1, 10, 2, 7]
build_max_heap(A)
print("Max Heap:", A)
