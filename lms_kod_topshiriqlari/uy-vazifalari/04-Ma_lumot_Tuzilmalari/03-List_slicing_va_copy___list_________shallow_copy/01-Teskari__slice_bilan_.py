import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    reversed_elements = input_data[::-1]
    
    print(*(reversed_elements))
    
if __name__ == '__main__':
    main()