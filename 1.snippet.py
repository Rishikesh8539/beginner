def compute_squares(nums: list[int]) -> list[int]:
    """
    Compute the squares of the given list of integers.

    Parameters:
    nums (list[int]): A list of integers to be squared.

    Returns:
    list[int]: A list containing the squares of the input integers.
    """
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

squares_list1 = compute_squares(list1)
squares_list2 = compute_squares(list2)

print(squares_list1)
print(squares_list2)
