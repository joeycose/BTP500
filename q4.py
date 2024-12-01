# Main Author: Giuseppe Cosentino

from rich import print

class BookNode:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.left = None
        self.right = None

class LibraryBST:
    def __init__(self):
        self.root = None

    def insert(self, title, author, year):
        """Insert a new book node into the BST."""
        if not self.root:
            self.root = BookNode(title, author, year)
        else:
            self._insert(self.root, title, author, year)

    def _insert(self, node, title, author, year):
        # If title is the same, ignore to avoid duplicates
        if title < node.title:
            if node.left is None:
                node.left = BookNode(title, author, year)
            else:
                self._insert(node.left, title, author, year)
        elif title > node.title:
            if node.right is None:
                node.right = BookNode(title, author, year)
            else:
                self._insert(node.right, title, author, year)

    def search(self, title):
        """Search for a book by title."""
        return self._search(self.root, title)

    def _search(self, node, title):
        if node is None or node.title == title:
            return node
        if title < node.title:
            return self._search(node.left, title)
        return self._search(node.right, title)

    def in_order_traversal(self, node, result=None):
        """In-order traversal to list books in alphabetical order."""
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node)
            self.in_order_traversal(node.right, result)
        return result

    def pre_order_traversal(self, node, result=None):
        """Pre-order traversal to list books for saving structure."""
        if result is None:
            result = []
        if node:
            result.append(node)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result=None):
        """Post-order traversal to list books for deletion."""
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node)
        return result

# Example usage
if __name__ == "__main__":
    library = LibraryBST()
    
    # Add few books
    library.insert("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.insert("To Kill a Mockingbird", "Harper Lee", 1960)
    library.insert("Pride and Prejudice", "Jane Austen", 1813)
    library.insert("1984", "George Orwell", 1949)
    library.insert("Moby-Dick", "Herman Melville", 1851)
    library.insert("The Catcher in the Rye", "J.D. Salinger", 1951)
    library.insert("War and Peace", "Leo Tolstoy", 1869)
    library.insert("Ulysses", "James Joyce", 1922)

    # Search for a book
    print("\nSearch the book: The Great Gatsby")
    book = library.search("The Great Gatsby")
    if book:
        print(f"Found book: {book.title}, {book.author}, {book.year}")
    else:
        print("\nBook not found")

    # Display books in different traversal orders
    print("In-order Traversal:\n", [(b.title, b.author, b.year) for b in library.in_order_traversal(library.root)])
    print("Pre-order Traversal:\n", [(b.title, b.author, b.year) for b in library.pre_order_traversal(library.root)])
    print("Post-order Traversal:\n", [(b.title, b.author, b.year) for b in library.post_order_traversal(library.root)])