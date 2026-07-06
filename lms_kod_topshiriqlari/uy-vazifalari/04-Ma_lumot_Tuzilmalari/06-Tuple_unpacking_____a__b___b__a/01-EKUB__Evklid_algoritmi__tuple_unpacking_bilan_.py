import sys

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    
    a = int(input_lines[0])
    b = int(input_lines[1]) if len(input_lines) > 1 else int(input_lines[0])
    
    while b != 0:
        a, b = b, a % b
    print(a)
    
if __name__ == '__main__':
    main()