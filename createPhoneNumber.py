#Method 1
def create_phone_number1(n):
    chars = ["(", ") ", "-"]
    phone_number = ""
    slice_list = [n[slice(0,3)], n[slice(3,6)], n[slice(6, len(n))]]
    for x in range(3):
        phone_number += chars[x] + ''.join(map(str,slice_list[x]))
    return phone_number

#Method 2
def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number2(numbers))