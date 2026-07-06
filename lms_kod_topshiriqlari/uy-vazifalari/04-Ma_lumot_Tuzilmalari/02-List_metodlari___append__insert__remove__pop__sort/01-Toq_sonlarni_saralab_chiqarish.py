import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    numbers = [int(x) for x in input_data[1:n+1]]
    
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_numbers.sort()
    
    print(*(odd_numbers))
    
if __name__ == '__main__':
    main()