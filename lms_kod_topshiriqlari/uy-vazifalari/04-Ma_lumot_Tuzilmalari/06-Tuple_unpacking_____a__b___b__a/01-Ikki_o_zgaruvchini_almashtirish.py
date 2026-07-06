import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    x = int(input_data[0])
    y = int(input_data[1])
    
    x, y = y, x
    
    print(x, y)
    
if __name__ == '__main__':
    main()