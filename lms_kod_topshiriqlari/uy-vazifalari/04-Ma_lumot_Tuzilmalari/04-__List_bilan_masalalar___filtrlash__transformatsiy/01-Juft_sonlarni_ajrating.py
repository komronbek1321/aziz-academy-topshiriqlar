import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    numbers = [int(x) for x in input_data]
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    print(*(even_numbers))
    
if __name__ == '__main__':
    main()