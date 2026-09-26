
# Made by : Yassine ikoubazene

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True
    n = len(arr1)
    mix = arr2 + arr2
    for i in range(n):
        if mix[i: n + i] == arr1:
            return True
    return False
    