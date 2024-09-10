def print_list_elements(lst):
    """
    Recursively prints all elements in a list.
    
    Args:
        lst (list): The list to print elements from.
    """
    # Base case: if the list is empty, stop recursion
    if not lst:
        return
    
    # Print the first element of the list
    print(lst[0])
    
    # Recursive call with the rest of the list
    print_list_elements(lst[1:])

# Example usage:
my_list = [1, 2, 3, 4, 5]
print_list_elements(my_list)