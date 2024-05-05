# 4. Write a Python function to get the largest number,
# smallest num and sum of all from a list

def list_stats(lst):
  

  largest = max(lst)
  smallest = min(lst)
  sum_elements = sum(lst)
  return smallest, largest, sum_elements


# Example usage:

print(list_stats([1, 2, 3, 4, 5]))






