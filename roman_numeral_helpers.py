roman = ['I', 'IV', 'V','X', 'L' ,'C', 'C', 'D', 'M']
numericals = [1,4,5,10,50,100,500,1000]
num_rom_dict = {k:v for k,v in zip(roman, numericals)}
rom_num_dict = {k:v for k,v in zip(numericals, roman)}

rom_num = lambda r: sum([num_rom_dict[s] for s in r])

def to_roman(val):
    if num in numericals:
        return rom_num_dict[num]