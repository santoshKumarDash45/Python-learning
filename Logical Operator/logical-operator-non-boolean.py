#  =========================== AND OPERATOR ===========================================
print(10 and 20)        # 10 is non-zero (truthy), so 'and' evaluates and returns the second operand: 20

# Here answer will be 20 as 10 is non-zero so according to and operator 
# if x is True then answer will be y and 
# if x is false means x is zero then answer will be y

print(0 and 20)         # 0 is falsy, so 'and' short-circuits and returns the first operand: 0

# Here answer will be false then answer will be o

print('' and 'santosh') # '' is falsy (empty string), so 'and' short-circuits and returns the first operand: ''

# Here answer will be empty string as here first parameter is empty string means False then 
# in and operator if x is false then answer will be y


# ================= OR OPERATOR ======================================

print(10 or 20)         # 10 is truthy, so 'or' short-circuits and returns the first operand: 10

# Here answer will be 10 as 10 is non-zero so according to or operator 
# if x is True then answer will be x and 
# if x is false means x is zero then answer will be y

print(0 or 20)          # 0 is falsy, so 'or' evaluates and returns the second operand: 20

# Here answer will be 20 as  according to or operator 
# if x is True then answer will be x and 
# if x is false means x is zero then answer will be y
