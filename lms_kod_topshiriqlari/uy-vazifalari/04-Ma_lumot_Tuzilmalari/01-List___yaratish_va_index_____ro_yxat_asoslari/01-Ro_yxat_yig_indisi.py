
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    total_sum = 0
    for num_str in input_data:
        total_sum += int(num_str)
        
    print(total_sum)
    
if __name__ == '__main__':
    main()