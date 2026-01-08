def hollow_square(n):

    for row in range(n):
        for col in range(n):
            if row == 0 or row == n - 1 or col == 0 or col == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print(hollow_square(5))

def number_pattern(n):
     result = ""
     for row in range(1, n):

        for col in range(1, row + 1):
            print(col, end="")
            result += "\n"
        print()
print(number_pattern(5))

# # Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    for row in range(1, n):
        print(row, end="")

        print()
print(sum_of_natural_numbers(6))

# # Example for n = 4:
# #    *
# #   ***
# #  *****
# # *******
def centered_star_pyramid(n):
    return ""
