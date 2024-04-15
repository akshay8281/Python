def calculate_area(length, width):
  """This function calculates the area of a rectangle."""
  area = length * width
  return area

# Get user input for length and width
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Call the function and print the result
area = calculate_area(length, width)
print("The area of the rectangle is", area)
