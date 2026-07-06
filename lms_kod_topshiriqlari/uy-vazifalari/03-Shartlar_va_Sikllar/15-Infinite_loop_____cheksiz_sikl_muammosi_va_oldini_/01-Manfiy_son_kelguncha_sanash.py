import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    count = 0
    for num_str in input_data:
        num = int(num_str)
        if num < 0:
            break
        count += 1
        
    print(count)
    
if __name__ == '__main__':
    main()