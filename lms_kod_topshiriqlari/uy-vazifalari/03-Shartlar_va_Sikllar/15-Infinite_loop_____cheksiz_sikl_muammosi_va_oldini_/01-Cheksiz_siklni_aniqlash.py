import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    start = int(input_data[0])
    step = int(input_data[1])
    
    if step <= 0:
        if start >= 100:
            print(0)
        else:
            print("CHEKSIZ")
    else:
        current = start
        steps_count = 0
        while current < 100:
            current += step
            steps_count += 1
        print(steps_count)
            
if __name__ == '__main__':
    main()