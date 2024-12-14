# Data barang belanjaan
items = [
    {"name": "Apel", "price": 15000},
    {"name": "Telur", "price": 20000},
    {"name": "Susu", "price": 25000},
    {"name": "Beras", "price": 50000},
    {"name": "Roti", "price": 10000},
]

def display_items(items):
    if not items:
        print("Daftar barang kosong.")
        return

    print(f"{'No':<4} {'Barang':<10} {'Harga':<10}")
    print("-" * 30)
    for i, item in enumerate(items, start=1):
        print(f"{i:<4} {item['name']:<10} Rp {item['price']:<10,}")

def bubble_sort(array):
    n = len(array)
    sorted_array = array[:]
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_array[j]["price"] > sorted_array[j + 1]["price"]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
    return sorted_array

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_array = []
    while left and right:
        if left[0]["price"] < right[0]["price"]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    sorted_array.extend(left)
    sorted_array.extend(right)
    return sorted_array

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    left = [item for item in array[:-1] if item["price"] <= pivot["price"]]
    right = [item for item in array[:-1] if item["price"] > pivot["price"]]
    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    print("Daftar Barang Belanjaan (Sebelum Diurutkan):")
    display_items(items)

    print("\nHasil Pengurutan dengan Bubble Sort:")
    sorted_items_bubble = bubble_sort(items)
    display_items(sorted_items_bubble)

    print("\nHasil Pengurutan dengan Merge Sort:")
    sorted_items_merge = merge_sort(items)
    display_items(sorted_items_merge)

    print("\nHasil Pengurutan dengan Quick Sort:")
    sorted_items_quick = quick_sort(items)
    display_items(sorted_items_quick)

if __name__ == "__main__":
    main()