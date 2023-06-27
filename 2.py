import time
import sys
import itertools

# Representasi matriks ketetanggaan dari graf
graph1 = {
    'a': {'a': 0, 'b': 12, 'c': 10, 'd': 0, 'e': 0, 'f': 0, 'g': 12},
    'b': {'a': 12, 'b': 0, 'c': 8, 'd': 12, 'e': 0, 'f': 0, 'g': 0},
    'c': {'a': 10, 'b': 8, 'c': 0, 'd': 11, 'e': 3, 'f': 0, 'g': 9},
    'd': {'a': 0, 'b': 12, 'c': 11, 'd': 0, 'e': 11, 'f': 10, 'g': 0},
    'e': {'a': 0, 'b': 0, 'c': 3, 'd': 11, 'e': 0, 'f': 6, 'g': 7},
    'f': {'a': 0, 'b': 0, 'c': 0, 'd': 10, 'e': 6, 'f': 0, 'g': 9},
    'g': {'a': 12, 'b': 0, 'c': 9, 'd': 0, 'e': 7, 'f': 9, 'g': 0}
}

graph2 = {
    'a': {'b': 12, 'c': 10, 'g': 12},
    'b': {'a': 12, 'c': 8, 'd': 12},
    'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
    'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'d': 10, 'e': 6, 'g': 9},
    'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
}

def tsp(graph1):
    start_time = time.time()

    # Mengumpulkan semua simpul kecuali simpul awal
    nodes = list(graph1.keys())
    nodes.remove('a')

    # Menggunakan itertools untuk menghasilkan semua kemungkinan permutasi jalur
    all_permutations = list(itertools.permutations(nodes))
    shortest_path = None
    shortest_distance = sys.maxsize

    # Menghitung jarak untuk setiap permutasi jalur dan mencari yang terpendek
    for permutation in all_permutations:
        distance = graph1['a'][permutation[0]]

        for i in range(len(permutation) - 1):
            distance += graph1[permutation[i]][permutation[i+1]]

        distance += graph1[permutation[-1]]['a']  # Menambahkan bobot dari simpul terakhir ke simpul awal

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = permutation

        print("Permutasi:", ' -> '.join(['a'] + list(permutation)) + ' -> a', "| Jarak:", distance)

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nShortest Path:", ' -> '.join(['a'] + list(shortest_path)) + ' -> a')
    print("Jarak Terpendek:", shortest_distance)
    print("Waktu eksekusi:", execution_time, "seconds")

def dijkstra(graph2, start):
    start_time = time.time()

    # Inisialisasi jarak terpendek untuk setiap simpul dengan tak terhingga
    distances = {node: float('inf') for node in graph2}
    # Set jarak terpendek dari simpul awal ke simpul awal sebagai 0
    distances[start] = 0
    # Set simpul yang belum dikunjungi
    unvisited = set(graph2)

    while unvisited:
        # Pilih simpul dengan jarak terpendek saat ini
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        # Periksa tetangga-tetangga dari simpul saat ini
        for neighbor, weight in graph2[current_node].items():
            # Perbarui jarak terpendek jika ditemukan jalur yang lebih pendek
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        print("Jarak:", distances)

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nShortest Distances:")
    for node, distance in distances.items():
        print("Dari", start, "Ke", node, ": Jarak =", distance)

    print("Waktu Eksekusi:", execution_time, "seconds")

def main():
    while True:
        print("\n--- Shortest Path Calculation ---")
        print("1. TSP (Traveling Salesman Problem)")
        print("2. Dijkstra's Algorithm")
        print("0. Keluar")

        choice = input("Masukkan Pilihan Anda: ")

        if choice == '1':
            print("\n--- TSP (Traveling Salesman Problem) ---")
            tsp(graph1)
        elif choice == '2':
            print("\n--- Dijkstra's Algorithm ---")
            start_node = input("Masukkan simpul awal: ")
            dijkstra(graph2, start_node)
        elif choice == '0':
            break
        else:
            print("Pilihan tidak sah. Silakan coba lagi.")

if __name__ == '__main__':
    main()