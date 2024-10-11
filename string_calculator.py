import re
def add(numbers):
    if numbers == "":
        return 0    
   
    numbers = numbers.replace('\\n', '\n') 
    delimiter = ","
    numbers = numbers.replace('\n', delimiter)    
    replaced_string = re.sub(r'[^\w]', ',', numbers)       
    number_list = [value for value in replaced_string.split(',') if value]    
    total = 0
    negatives = []    
    for num in number_list:
        try:
            n = int(num)  
        except ValueError:
            raise ValueError(f"Invalid input '{num}': must be a number.")
        
        if n < 0:
            negatives.append(n)
        total += n

    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

    return total

input_val = input("Input : ")
try:
    res = add(input_val)
    print("Output :", res)
except ValueError as e:
    print("Error:", e)
