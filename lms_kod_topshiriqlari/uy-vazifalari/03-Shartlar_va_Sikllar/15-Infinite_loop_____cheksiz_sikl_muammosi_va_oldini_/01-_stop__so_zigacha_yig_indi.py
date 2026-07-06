import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    total_sum = 0
    for item in input_data:
        if item == "stop":
            break
        total_sum += int(item)
        
    print(total_sum)
    
if __name__ == '__main__':
    main()