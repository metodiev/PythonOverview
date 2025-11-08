import sys

def list_and_collection_exercise():
    #Create a list of five numbers
    numbers = [1, 100, 115, 200, 5]
    print(f"Original list: {numbers}")

    #Append two new numbers and remove one.
    numbers.append(0)
    numbers.append(-25)
    numbers.remove(115)
    print(f"Modified List (added 0, and -25; removed 115): {numbers})")

    #Sort the list in descending order.
    numbers.sort(reverse=True)
    print(f"Sorted list in descending order: {numbers}")
    #print(f"Largest number: {numbers[0]}")

    #Create a new list using comprehension that contains only even numbers from it.
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers from the list: {even_numbers}")

def list_size_test():
    test_array = [1, 2, 3]
    print(f"Size of th test array before appending: {len(test_array)}")
    print(f"Size of the test array: {sys.getsizeof(test_array)} bytes")
    test_array.append(4)
    print(f"Size of th test array before appending: {len(test_array)}")
    print(f"Size of the test array: {sys.getsizeof(test_array)} bytes")
    test_array.append(44)
    test_array.append(2)
    print(f"Size of the test array: {sys.getsizeof(test_array)} bytes")

if __name__ == "__main__":
    list_and_collection_exercise()
    list_size_test()