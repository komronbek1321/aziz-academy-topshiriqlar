import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    original_nums = [int(x) for x in input_data]
    
    copied_nums = original_nums[:]
    copied_nums.sort()
    
    print(*(original_nums))
    print(*(copied_nums))
    
if __name__ == '__main__':
    main()