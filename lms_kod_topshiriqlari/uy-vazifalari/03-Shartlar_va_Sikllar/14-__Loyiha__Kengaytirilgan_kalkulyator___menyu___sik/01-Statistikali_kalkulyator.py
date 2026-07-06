import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    valid_count = 0
    total_sum = 0
    
    while True:
        try:
            op = int(next(iterator))
        except StopIteration:
            break
            
        if op == 0:
            break
            
        try:
            a = int(next(iterator))
            b = int(next(iterator))
        except StopIteration:
            break
            
        valid = False
        res = 0
        
        if op == 1:
            res = a + b
            valid = True
        elif op == 2:
            res = a - b
            valid = True
        elif op == 3:
            res = a * b
            valid = True
        elif op == 4:
            if b != 0:
                res = a // b
                valid = True
                
        if valid:
            print(res)
            valid_count += 1
            total_sum += res
            
    print(f"Amallar: {valid_count}")
    print(f"Natijalar yig'indisi: {total_sum}")
    
if __name__ == '__main__':
    main()