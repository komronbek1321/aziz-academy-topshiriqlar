import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    max_result = None
    
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
        elif op == 5:
                res = a ** b
                valid = True
        elif op == 6:
                if b != 0:
                    res = a % b
                    valid = True
                    
        if valid:
            print(res)
            if max_result is None or res > max_result:
                max_result = res
                
    if max_result is not None:
        print(f"Eng katta natija: {max_result}")
        
if __name__ == '__main__':
    main()