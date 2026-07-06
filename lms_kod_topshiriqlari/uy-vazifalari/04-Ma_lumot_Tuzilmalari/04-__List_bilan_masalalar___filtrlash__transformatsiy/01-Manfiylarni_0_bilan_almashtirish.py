import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    result = []
    for x in input_data:
        num = int(x)
        if num < 0:
            result.append(0)
        else:
            result.append(num)
            
    print(*(result))
    
if __name__ == '__main__':
    main()