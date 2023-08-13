# Example 1: Basic lambda function
addition = lambda x, y: x + y
print(addition(3, 5))  # Output: 8

# Example 2: Sorting a list of tuples based on the second element
students = [("Alice", 25), ("Bob", 32), ("Charlie", 28)]
students.sort(key=lambda x: x[1])
print(students)  # Output: [('Alice', 25), ('Charlie', 28), ('Bob', 32)]

# Example 3: Using lambda with built-in functions
numbers = [1, 4, 3, 2, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [4, 2]

# Example 4: Combining lambda with map function
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 16, 9, 4, 25]




# In the above code:

# Example 1 demonstrates a basic lambda function that takes two arguments x and y and returns their sum.
# Example 2 shows how lambda can be used as a key function in the sort() method to sort a list of tuples based on the second element.
# Example 3 uses lambda with the filter() function to filter even numbers from a list.
# Example 4 combines lambda with the map() function to square each element of a list.
# Lambda functions are useful when you need a small, concise function without the need for a formal function declaration.
# However, for more complex or larger functions, it is generally recommended to use a regular named function defined with 
# def for better readability and maintainability