import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    words_tuple = tuple(input_data)
    
    print(len(words_tuple))
    
if __name__ == '__main__':
    main()