import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    print(input_data[0])
    print(input_data[-1])
    
if __name__ == '__main__':
    main()