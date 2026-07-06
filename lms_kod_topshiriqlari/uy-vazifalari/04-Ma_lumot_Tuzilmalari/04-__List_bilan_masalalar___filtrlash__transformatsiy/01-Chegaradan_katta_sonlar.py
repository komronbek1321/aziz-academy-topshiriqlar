import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    elements = [int(x) for x in input_data[:-1]]
    t = int(input_data[-1])
    
    result = [num for num in elements if num > t]
    
    print(*(result))
    
if __name__ == '__main__':
    main()