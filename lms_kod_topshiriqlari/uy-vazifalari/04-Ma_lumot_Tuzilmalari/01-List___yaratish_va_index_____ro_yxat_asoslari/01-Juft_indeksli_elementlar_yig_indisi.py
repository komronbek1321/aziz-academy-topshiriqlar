import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    total_sum = 0
    for i in range(len(input_data)):
        if i % 2 == 0:
            total_sum += int(input_data[i])
            
    print(total_sum)
    
if __name__ == '__main__':
    main()