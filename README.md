# 42 Exam - Rank 04 (Python Subjects)

> **Source:** [https://rank04.42exam.net/](https://rank04.42exam.net/)  
> **Language:** Python 3  
> **Total Subjects:** 7

> [!IMPORTANT]
> Exam tasks may have slight variations depending on your campus or pool (e.g., alternate function names or signatures). Always carefully read the official subject prompt during your exam!

## Table of Contents

| # | Subject Name | Level | Difficulty | Target File | Forbidden Functions |
|:---:|---|:---:|:---:|---|---|
| 1 | [py_array_rotation_detector](#py-array-rotation-detector) | Level 1 | Easy | `py_array_rotation_detector.py` | `collections.deque.rotate()` |
| 2 | [py_constellation_mapper](#py-constellation-mapper) | Level 1 | Medium | `py_constellation_mapper.py` | *None* |
| 3 | [py_list_intersection_finder](#py-list-intersection-finder) | Level 1 | Easy | `py_list_intersection_finder.py` | *None* |
| 4 | [py_merge_sorted_lists](#py-merge-sorted-lists) | Level 2 | Medium | `py_merge_sorted_lists.py` | `sorted()`, `.sort()`, `heapq.merge()` |
| 5 | [py_palindrome_partitioner](#py-palindrome-partitioner) | Level 3 | Hard | `py_palindrome_partitioner.py` | *None* |
| 6 | [py_package_dependency_resolver](#py-package-dependency-resolver) | Level 3 | Hard | `py_package_dependency_resolver.py` | `graphlib.TopologicalSorter` |
| 7 | [py_sliding_window_maximum](#py-sliding-window-maximum) | Level 4 | Hard | `py_sliding_window_maximum.py` | *None* |

---

## 1. py_array_rotation_detector

- **Level:** 1
- **Difficulty:** Easy
- **File to submit:** `py_array_rotation_detector.py`
- **Forbidden functions / modules:** `collections.deque.rotate()`

### Function Signature
```python
def array_rotation_detector(arr1: list, arr2: list) -> bool:
```

### Subject Description
Determine if array2 is a rotation of array1. A rotation shifts elements cyclically while maintaining relative order.

- Return True if array2 is a valid rotation of array1
- Return False otherwise or if array lengths differ
- Handle empty arrays (two empty arrays are considered valid rotations)

### Examples
```python
>>> array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])
True
>>> array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])
True
>>> array_rotation_detector([1, 2, 3], [3, 2, 1])
False
>>> array_rotation_detector([1, 2], [1, 2, 3])
False
>>> array_rotation_detector([], [])
True
```

### Key Insights & Edge Cases
- **Edge Cases:** Both arrays empty (`[]`, `[]`) must return `True`. Arrays with differing lengths must immediately return `False`.
- **Constraint:** Do not use `collections.deque.rotate()`.
- **Approach:** Concatenating `arr2 + arr2` produces all cyclic rotations as contiguous slices of length $N$.

### Reference Implementation
```python
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True
    n = len(arr1)
    doubled = arr2 + arr2
    for i in range(n):
        if doubled[i : i + n] == arr1:
            return True
    return False
```

---

## 2. py_constellation_mapper

- **Level:** 1
- **Difficulty:** Medium
- **File to submit:** `py_constellation_mapper.py`
- **Forbidden functions / modules:** None

### Function Signature
```python
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
```

### Subject Description
Write a function that maps a constellation of stars onto a grid and returns the visual representation as a list of strings.

The function should:
- Take a list of star coordinates as tuples (row, col) and grid size as integer
- Return a list of strings representing the grid
- Stars are represented by '*' and empty spaces by '.'
- Grid coordinates start from (0, 0) at top-left
- Ignore coordinates outside the grid boundaries
- Handle duplicate coordinates (star appears only once)

### Examples
```python
>>> constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
['*..', '.*.', '..*']
>>> constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
['.*.', '***', '.*.']
>>> constellation_mapper([], 2)
['..', '..']
>>> constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
['*.', '.*']
>>> constellation_mapper([(0, 0), (5, 5)], 3)
['*..', '...', '...']
>>> constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)
['...', '***', '...']
```

### Key Insights & Edge Cases
- **Edge Cases:** Empty star list (`[]`), duplicate star coordinates (place only one `*`), and star coordinates lying outside the grid bounds ($r < 0$, $r \ge \text{dim}$, $c < 0$, $c \ge \text{dim}$) which must be discarded.
- **Coordinates:** `(0, 0)` is top-left, where the first element of tuple is row (y) and second is column (x).

### Reference Implementation
```python
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    grid = [["." for _ in range(dim)] for _ in range(dim)]
    for r, c in stars:
        if 0 <= r < dim and 0 <= c < dim:
            grid[r][c] = "*"
    return ["".join(row) for row in grid]
```

---

## 3. py_list_intersection_finder

- **Level:** 1
- **Difficulty:** Easy
- **File to submit:** `py_list_intersection_finder.py`
- **Forbidden functions / modules:** None

### Function Signature
```python
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
```

### Subject Description
Find common elements present in all given integer lists. Return unique common elements sorted in ascending order.

- Return an empty list if any list is empty or if no common elements exist
- Preserve uniqueness in the output

### Examples
```python
>>> list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])
[2, 3]
>>> list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])
[4]
>>> list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])
[1, 2, 3]
>>> list_intersection_finder([[1, 2, 3], [4, 5, 6]])
[]
>>> list_intersection_finder([])
[]
>>> list_intersection_finder([[1, 2, 3], []])
[]
>>> list_intersection_finder([[5]])
[5]
```

### Key Insights & Edge Cases
- **Edge Cases:** If `lists` is empty, or if any inner list is empty, return an empty list `[]`.
- **Uniqueness & Sorting:** The output must contain only unique values and be sorted in ascending order.
- **Approach:** Use Python `set.intersection()` across all list sets, then return `sorted(list(common))`.

### Reference Implementation
```python
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists or any(len(lst) == 0 for lst in lists):
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common.intersection_update(lst)
    return sorted(list(common))
```

---

## 4. py_merge_sorted_lists

- **Level:** 2
- **Difficulty:** Medium
- **File to submit:** `py_merge_sorted_lists.py`
- **Forbidden functions / modules:** `sorted()`, `.sort()`, `heapq.merge()`

### Function Signature
```python
def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
```

### Subject Description
Write a function that merges multiple sorted lists into one sorted list while maintaining the sort order efficiently.

The function should:
- Take a list of sorted integer lists as input
- Return a single merged list in ascending order
- Preserve all duplicate elements in the final result
- Handle empty lists and empty input gracefully
- Maintain optimal efficiency for large inputs

### Examples
```python
>>> merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> merge_sorted_lists([[5], [1, 3], [2, 4]])
[1, 2, 3, 4, 5]
>>> merge_sorted_lists([[1, 1, 2], [2, 3, 3]])
[1, 1, 2, 2, 3, 3]
>>> merge_sorted_lists([[], [1, 2, 3]])
[1, 2, 3]
>>> merge_sorted_lists([[]])
[]
>>> merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])
[-5, -3, -1, 0, 2, 4]
>>> merge_sorted_lists([[10], [10], [10]])
[10, 10, 10]
```

### Key Insights & Edge Cases
- **Constraint:** Strictly forbid `sorted()`, `.sort()`, and `heapq.merge()`.
- **Duplicates:** Preserve all duplicate numbers from all input lists.
- **Approach:** Implement a multi-way merge with a Min-Heap (`heapq.heappush` and `heapq.heappop`) tracking `(value, list_index, element_index)`. This achieves optimal $O(N \log K)$ time complexity where $K$ is the number of lists.

### Reference Implementation
```python
import heapq

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
    return result
```

---

## 5. py_palindrome_partitioner

- **Level:** 3
- **Difficulty:** Hard
- **File to submit:** `py_palindrome_partitioner.py`
- **Forbidden functions / modules:** None

### Function Signature
```python
def palindrome_partitioner(s: str) -> int:
```

### Subject Description
Given a string s, find the minimum number of cuts needed to partition it such that every resulting substring is a palindrome.

- Return the minimum number of cuts (an integer)
- A string of length 1 requires 0 cuts
- An empty string requires 0 cuts

### Examples
```python
>>> palindrome_partitioner("aab")
1
>>> palindrome_partitioner("aba")
0
>>> palindrome_partitioner("abc")
2
```

### Key Insights & Edge Cases
- **Edge Cases:** Length 0 (empty string) and length 1 both require `0` cuts.
- **Approach:** Dynamic programming. Precompute a 2D table `is_pal[i][j]` indicating whether `s[i:j+1]` is a palindrome. Then maintain `dp[i]`, the minimum cuts for prefix `s[0:i+1]`. If `s[0:i+1]` is a palindrome, cuts = 0; otherwise test all partition points $j < i$.

### Reference Implementation
```python
def palindrome_partitioner(s: str) -> int:
    n = len(s)
    if n <= 1:
        return 0

    # is_pal[i][j] is True if substring s[i:j+1] is a palindrome
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True

    # dp[i] = minimum cuts needed for substring s[0:i+1]
    dp = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            dp[i] = i
            for j in range(i):
                if is_pal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    return dp[n - 1]
```

---

## 6. py_package_dependency_resolver

- **Level:** 3
- **Difficulty:** Hard
- **File to submit:** `py_package_dependency_resolver.py`
- **Forbidden functions / modules:** `graphlib.TopologicalSorter`

### Function Signature
```python
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
```

### Subject Description
Write a function that determines a valid package installation order by resolving dependencies. Use topological sorting to ensure dependencies are installed before the packages that require them.

The function should:
- Take a dictionary where keys are package names and values are lists of dependencies
- Return packages in installation order (dependencies first)
- Return empty list if no valid order exists (circular dependencies)
- Handle empty input and isolated dependency chains
- Ignore references to packages not in the input dictionary

### Examples
```python
>>> package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})
["driver", "database", "app"]
>>> package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})
["A", "B", "C"]
>>> package_dependency_resolver({})
[]
>>> package_dependency_resolver({"X": ["Y"], "Y": ["X"]})
[]
>>> package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})
["api", "web", "backend", "frontend"]
```

### Key Insights & Edge Cases
- **Constraint:** Do not use `graphlib.TopologicalSorter`.
- **Key Requirement:** Packages referenced in dependency lists that are NOT present as keys in the dictionary must be ignored.
- **Cycle Detection:** If there is a circular dependency (e.g. `X -> Y` and `Y -> X`), no valid installation order exists; return `[]`.
- **Approach:** Kahn's algorithm (BFS with in-degrees) or DFS cycle detection.

### Reference Implementation
```python
from collections import deque

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    # Filter dependencies to only include packages present in input
    in_degree = {pkg: 0 for pkg in packages}
    adj = {pkg: [] for pkg in packages}
    for pkg, deps in packages.items():
        valid_deps = [d for d in deps if d in packages]
        in_degree[pkg] = len(valid_deps)
        for d in valid_deps:
            adj[d].append(pkg)

    # Kahn's algorithm for topological sorting
    queue = deque([pkg for pkg, deg in in_degree.items() if deg == 0])
    order = []
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    # If order does not contain all packages, a cycle exists
    if len(order) != len(packages):
        return []
    return order
```

---

## 7. py_sliding_window_maximum

- **Level:** 4
- **Difficulty:** Hard
- **File to submit:** `py_sliding_window_maximum.py`
- **Forbidden functions / modules:** None

### Function Signature
```python
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
```

### Subject Description
Write a function that finds the maximum element in each sliding window of size k in an array. Return a list of maximums for each window position.

The function should:
- Slide a window of size k through the array
- Find the maximum element in each window position
- Return a list of maximum values
- Handle edge cases (empty array, k <= 0, k > array length)
- Return empty list for invalid inputs

### Examples
```python
>>> sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
[3, 3, 5, 5, 6, 7]
>>> sliding_window_maximum([1, 2, 3, 4, 5], 2)
[2, 3, 4, 5]
>>> sliding_window_maximum([5, 4, 3, 2, 1], 1)
[5, 4, 3, 2, 1]
>>> sliding_window_maximum([1, 2, 3], 3)
[3]
>>> sliding_window_maximum([1, 2, 3], 4)
[]
>>> sliding_window_maximum([], 2)
[]
>>> sliding_window_maximum([1, 2, 3], 0)
[]
```

### Key Insights & Edge Cases
- **Edge Cases:** Empty array (`[]`), $k \le 0$, or $k > \text{len}(nums)$ must return `[]`.
- **Efficiency:** A naive slice-max approach runs in $O(N \times K)$. Using a monotonic deque achieves optimal $O(N)$ time complexity.

### Reference Implementation
```python
from collections import deque

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    dq = deque()  # stores indices of candidate maximums in monotonically decreasing order
    res = []

    for i in range(len(nums)):
        # Remove elements outside current sliding window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements as they are dominated by nums[i]
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Append maximum (front of deque) once first window is formed
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res
```

---
