def is_disarium(num):
    return num == sum(int(digit) ** (idx + 1) for idx, digit in enumerate(str(num)))

def disarium_in_range(start, end):
    return [num for num in range(start, end + 1) if is_disarium(num)]
start = int(input("Enter the start of the range: "))

end = int(input("Enter the end of the range: "))
result = disarium_in_range(start, end)
print(f"Disarium numbers between {start} and {end} are: {result}")