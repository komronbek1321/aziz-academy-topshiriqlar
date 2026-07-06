import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    elements = input_data[:-2]
    a = int(input_data[-2])
    b = int(input_data[-1])
    
    sliced_elements = elements[a:b]
    
    print(*(sliced_elements))
    
if __name__ == '__main__':
    main()