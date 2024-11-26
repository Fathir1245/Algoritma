import random

data = [random.randint(0, 100) for _ in range(50)]

def naive_bayes_sort(arr):
    count = [0] * 101
    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

if __name__ == "__main__":
    print("Original Data:", data)
    sorted_data = naive_bayes_sort(data)
    print("Naive Bayes Sorted Data:", sorted_data)
