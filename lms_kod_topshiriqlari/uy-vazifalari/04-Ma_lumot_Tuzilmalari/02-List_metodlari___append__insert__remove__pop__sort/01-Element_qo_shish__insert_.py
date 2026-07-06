import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    elements = input_data[:-2]
    p = int(input_data[-2])
    x = input_data[-1]
    
    elements.insert(p, x)
    
    print(*(elements))
    
if __name__ == '__main__':
    main()