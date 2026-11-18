def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()
# print(numbers)  O/P- <generator object get_numbers at 0x0000029A784653C0>
for num in numbers:
    print(num)

# 1
# 2
# 3
# 4
# 5

def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

# When the next value is requested, it resumes from where it stopped.
# Conceptually:
"""
yield 10
   ↓
pause
   ↓
resume
   ↓
yield 20
   ↓
pause
   ↓
resume
   ↓
yield 30
"""

# When would you prefer a generator?
# 1. Data is very large
# 2. Processing data one by one
# 3. Reading large files