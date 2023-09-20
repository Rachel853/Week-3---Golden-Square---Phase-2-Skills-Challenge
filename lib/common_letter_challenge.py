def get_most_common_letter(text):
    counter = {}
    print(f"Text provided is: {text}")
    for char in text:
        if char.isalpha():
            print(f"The current char is {char}")
            counter[char] = counter.get(char, 0) + 1
            print(f"The current counter is {counter}")
    sorted_counter = sorted(counter.items(), key=lambda item: item[1])
    mystery_value = sorted_counter[-1][0]
    print(sorted_counter)
    print(sorted_counter[0])
    print(mystery_value)
    return mystery_value


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")