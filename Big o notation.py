
                    #   (BIG O NOTATIONS)



# Big O notation is a mathematical way to describe how an algorithm's
# execution time or memory usage scales as the input size grows


# To measure how well an algorithm scales, developers look at its behavior as the input size grows 
# (\(N\)). This math is summarized using Big O Notation:

# • \(O(1)\) — Constant Time: Performance stays identical regardless of input size (e.g., reading an array item by index).
# ----------------------
# • \(O(\log N)\) — Logarithmic Time: The input space is cut in half at each step, making it highly efficient (e.g., Binary Search).
# ------------------------
# • \(O(N)\) — Linear Time: The execution time scales directly with the data size (e.g., looking for a specific item in an unsorted list).
# ----------------------------
# • \(O(N^2)\) — Quadratic Time: Performance drops sharply because of nested loops scanning the data multiple times (e.g., Bubble Sort)