import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    elements = input_data[:-1]
    k = int(input_data[-1])
    
    elements_tuple = tuple(elements)
    
    print(elements_tuple[k])
    
if __name__ == '__main__':
    main()