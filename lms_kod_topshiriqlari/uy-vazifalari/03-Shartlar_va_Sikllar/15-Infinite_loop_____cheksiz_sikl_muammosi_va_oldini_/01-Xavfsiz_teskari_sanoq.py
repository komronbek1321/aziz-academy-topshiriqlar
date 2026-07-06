import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    while n > 0:
        print(n)
        n -= 1
        
    print("BOOM")
    
if __name__ == '__main__':
    main()