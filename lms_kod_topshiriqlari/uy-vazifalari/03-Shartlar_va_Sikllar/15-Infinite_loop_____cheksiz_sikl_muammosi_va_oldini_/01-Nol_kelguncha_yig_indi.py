import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    total_sum = 0
    for num_str in input_data:
        num = int(num_str)
        if num == 0:
            break
        total_sum += num
    print(total_sum)
    
if __name__ == '__main__':
    main()