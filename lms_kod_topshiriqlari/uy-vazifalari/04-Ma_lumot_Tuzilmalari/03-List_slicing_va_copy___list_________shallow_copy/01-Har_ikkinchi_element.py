import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    every_second_element = input_data[::2]
    
    print(*(every_second_element))
    
if __name__ == '__main__':
    main()