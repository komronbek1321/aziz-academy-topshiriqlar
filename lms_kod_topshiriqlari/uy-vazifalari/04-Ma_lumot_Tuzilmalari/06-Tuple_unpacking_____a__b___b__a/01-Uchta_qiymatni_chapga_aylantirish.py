import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    
    a, b, c = b, c, a
    print(a, b, c)
    
if __name__ == '__main__':
    main()