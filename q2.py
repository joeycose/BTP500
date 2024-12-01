# Main Author: Giuseppe Cosentino

# Define the hash table as a dictionary
class StudentHashTable:
    def __init__(self):
        self.table = {}

    # Function to insert a student record
    def insert(self, student_id, name, gpa):
        if student_id in self.table:
            print(f"Student ID {student_id} already exists. Updating record.")
        self.table[student_id] = {'name': name, 'gpa': gpa}
        print(f"Inserted: {student_id} -> {name}, GPA: {gpa}")

    # Function to retrieve a student record by student ID
    def retrieve(self, student_id):
        if student_id in self.table:
            student = self.table[student_id]
            print(f"Retrieved: {student_id} -> {student['name']}, GPA: {student['gpa']}")
        else:
            print(f"Student ID {student_id} not found.")

    # Function to delete a student record by student ID
    def delete(self, student_id):
        if student_id in self.table:
            del self.table[student_id]
            print(f"Deleted student record with ID: {student_id}")
        else:
            print(f"Student ID {student_id} not found.")

# Example usage
# Initialize the hash table
students = StudentHashTable()

# Insert some student records
print(f"Add a Student Record: 101")
students.insert(101, "Alice", 3.8)
print(f"Add a Student Record: 102")
students.insert(102, "Bob", 3.5)
print(f"Add a Student Record: 103")
students.insert(103, "Charlie", 2.2)
print(f"Add a Student Record: 104")
students.insert(104, "Jane", 3.4)
print(f"Add a Student Record: 105")
students.insert(105, "John", 3.2)
print(f"Add a Student Record: 106")
students.insert(106, "Joe", 3.5)

# Retrieve a student record
print(f"Retrieve a Student Record: 101")
students.retrieve(101)
print(f"Retrieve a Student Record: 105")
students.retrieve(105)
print(f"Retrieve a Student Record: 106")
students.retrieve(106)

# Delete a student record
print(f"Delete a Student Record: 102")
students.delete(102)

# Attempt to retrieve a deleted record
print(f"Retrieve a Student Record that was deleted: 102")
students.retrieve(102)