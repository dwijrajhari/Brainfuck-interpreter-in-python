def Brainf(s, n = 10, debug = False):
    
    tape = [0]*n
    data_ptr = 0
    prog_ptr = 0
    loop_addr = []
    
    while prog_ptr<len(s):
        
        i = s[prog_ptr]
        
        if   i == '+':
            tape[data_ptr] = (tape[data_ptr]+1)%256
            
        elif i == '-':
            tape[data_ptr] = (tape[data_ptr]-1)%256
            
        elif i == '>':
            data_ptr = data_ptr+1
            if data_ptr >= n:
                print("Error: Illegal Memory Access. Program Terminated")
                break
                
        elif i == '<':
            data_ptr = data_ptr-1
            if data_ptr < 0:
                print("Error: Illegal Memory Access. Program Terminated")
                break
                
        elif i == '[':
            if tape[data_ptr] == 0:
                b_count = 1
                prog_ptr += 1
                while b_count:
                    if s[prog_ptr] == '[':
                        b_count += 1
                    elif s[prog_ptr] == ']':
                        b_count -= 1
                    prog_ptr += 1
                prog_ptr -= 1
            else:
                loop_addr.append(prog_ptr)
                
        elif i == ']':
            try:
                prog_ptr = loop_addr.pop()-1
            except IndexError:
                print("Error: Mismatched Brackets. Program Terminated")
                break
                
        elif i == '.':
            print(chr(tape[data_ptr]), end = '')
            
        elif i == ',':
            tape[data_ptr] = ord(input()[0])
            
        prog_ptr+=1
    return tape
