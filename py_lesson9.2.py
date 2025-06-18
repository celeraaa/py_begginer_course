def difference(numbers):
    if not numbers:
        return 0
    else:
        difference_result = max(numbers) - min(numbers)
        return  round(difference_result, 2)


numbers = [5, -5]
print(difference(numbers))