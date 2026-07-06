import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    input_data.reverse()
    
    print(*(input_data))
    
if __name__ == '__main__':
    main()