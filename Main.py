i = input("Enter the string: ")

try:
    float(i)
    print(f'The string {i} is numeric')
except:
    print(f'The string {i} is not numeric')
