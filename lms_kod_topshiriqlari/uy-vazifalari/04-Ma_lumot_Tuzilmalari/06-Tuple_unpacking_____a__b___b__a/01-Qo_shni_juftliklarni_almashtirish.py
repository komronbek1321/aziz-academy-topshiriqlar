import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nums = input_data
    
    for i in range(0, len(nums) - 1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]
        
    print(*(nums))
    
if __name__ == '__main__':
    main()