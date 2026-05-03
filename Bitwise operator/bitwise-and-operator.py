# Bitwise operators - can be applied to only int and bool type

print(10 & 20)          # bitwise AND of 10 (1010) and 20 (10100), result is 0 (no common set bits)

# Answer will be 0
print(10.5 & 20.6)      # TypeError: bitwise AND is not supported for float types

# Type error because both are float 

print('durge' & 'soft') # TypeError: bitwise AND is not supported for string types

# Type error because both are string values

print(4 & 5)            # bitwise AND of 4 (100) and 5 (101), result is 4 (100) - both bits must be 1

# Answer is 4 as if both bits are 1 then result is 1 or else 0

print(4 | 5)            # bitwise OR of 4 (100) and 5 (101), result is 5 (101) - at least one bit must be 1

# Answer is 5 as if atleast one bit is 1 then result is 1 or else 0

print(4 ^ 5)            # bitwise XOR of 4 (100) and 5 (101), result is 1 (001) - bits must be different

# Answer is 1 as if both bits are different then result is 1 or else 0
