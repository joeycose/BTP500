# Main Author: Giuseppe Cosentino

class Graph:
    def __init__(self, num_vertices):
        # Initialize the adjacency matrix with zeros
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Function to insert an edge
    def insert_edge(self, v1, v2):
        if v1 < self.num_vertices and v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1  # Undirected graph
            print(f"Edge added between {v1} and {v2}")
        else:
            print("Error: Vertex index out of bounds.")

    # Function to delete an edge
    def delete_edge(self, v1, v2):
        if v1 < self.num_vertices and v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0  # Undirected graph
            print(f"Edge removed between {v1} and {v2}")
        else:
            print("Error: Vertex index out of bounds.")

    # Function to display the adjacency matrix
    def display_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# Example usage
if __name__ == "__main__":
    # Initialize a graph with 13 vertices
    graph = Graph(13)

    # Insert some edges
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(1, 4)
    graph.insert_edge(2, 5)
    graph.insert_edge(2, 6)
    graph.insert_edge(3, 7)
    graph.insert_edge(3, 8)
    graph.insert_edge(4, 9)
    graph.insert_edge(4, 10)

    # Display the adjacency matrix
    graph.display_matrix()

    # Delete an edge
    graph.delete_edge(10, 11)  # This will show an error since 11 is out of bounds

    # Display the adjacency matrix again
    graph.display_matrix()