import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    x1 = int(input_data[0])
    y1 = int(input_data[1])
    x2 = int(input_data[2])
    y2 = int(input_data[3])
    
    distance_squared = (x2 - x1)**2 + (y2 - y1)**2
    
    print(distance_squared)
    
if __name__ == '__main__':
    main()