import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    reversed_data = input_data[::-1]
    print(*(reversed_data))
    
if __name__ == '__main__':
    main()