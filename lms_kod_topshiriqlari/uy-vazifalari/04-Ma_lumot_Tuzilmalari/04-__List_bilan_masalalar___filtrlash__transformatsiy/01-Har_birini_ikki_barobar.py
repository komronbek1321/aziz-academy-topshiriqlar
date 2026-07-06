import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    doubled_numbers = [int(num) * 2 for num in input_data]
    
    print(*(doubled_numbers))
    
if __name__ == '__main__':
    main()