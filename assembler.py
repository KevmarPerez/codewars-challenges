def simple_assembler(program):
        mylist = [elems.split() for elems in program]
        Registers = {'a':0, 'b': 0, 'c': 0}
        oplist = []
        for instr in mylist:
            oplist.append(instr[0])
            def func(op):
                if op == 'mov':
                    operand = int(instr[2]) if instr[2].isnumeric() else Registers[instr[2]]
                    print(operand)
                    Registers.update({instr[1]: operand})
                elif op == 'inc': 
                    Registers.update({instr[1]: Registers[instr[1]] + 1})
                elif op == 'dec': 
                    Registers.update({instr[1]: Registers[instr[1]] - 1})
                elif op == 'jnz':
                    while Registers[instr[1]] != 0:
                        func(oplist[len(oplist)+int(instr[2])-1])
            func(instr[0])
        return {a:b for a,b in Registers.items() if b != 0}

inpt = simple_assembler(['mov a 2','dec a','inc b','jnz a -2','dec c','mov a b', 'jnz c -5', 'jnz 0 1', 'mov c a'])
print(inpt)