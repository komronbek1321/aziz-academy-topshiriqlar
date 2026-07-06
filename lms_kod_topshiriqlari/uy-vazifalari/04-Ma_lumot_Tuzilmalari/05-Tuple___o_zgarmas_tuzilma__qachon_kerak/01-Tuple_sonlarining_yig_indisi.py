import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    numbers_tuple = tuple(int(x) for x in input_data)
    
    total_sum = 0
    for num in numbers_tuple:
        total_sum += num
    print(total_sum)
    
if __name__ == '__main__':
    main()