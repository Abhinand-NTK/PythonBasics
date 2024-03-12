def count_set_bits(num):
    count = 0
    while num:
        print("The num value in the every iteration :-",num)
        count += num & 1
        num >>= 1
    return count

# Example usage:
number = 2

set_bits_count = count_set_bits(number)
print(f"The number of set bits in {number} is {set_bits_count}")

number.bit_count()
