import sys

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    
    list1 = input_lines[0].split()
    list2 = input_lines[1].split() if len(input_lines) > 1 else []
    
    set2 = set(list2)
    
    result = []
    for x in list1:
        if x in set2 and x not in result:
            result.append(x)
            
    print(*(result))
    
if __name__ == '__main__':
    main()