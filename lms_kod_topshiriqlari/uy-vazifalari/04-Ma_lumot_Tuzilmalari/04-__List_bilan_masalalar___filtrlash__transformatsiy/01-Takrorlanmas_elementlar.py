import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    seen = set()
    result = []
    
    for x in input_data:
        if x not in seen:
            seen.add(x)
            result.append(x)
            
    print(*(result))
    
if __name__ == '__main__':
    main()