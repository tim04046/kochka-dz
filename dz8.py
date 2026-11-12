def process_list(input_list):
    assert len(input_list) >= 3, "List must contain at least 3 elements"
    print(f"List contains {len(input_list)} elements")


try:
    process_list([1, 2, 3, 4, 5])
except AssertionError as e:
    print(e)

try:
    process_list([1, 2])
except AssertionError as e:
    print(e)
