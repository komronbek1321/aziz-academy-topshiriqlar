import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    elements = input_data[:-1]
    k = int(input_data[-1])
    
    first_k_elements = elements[:k]
    
    print(*(first_k_elements))
    
if __name__ == '__main__':
    main()