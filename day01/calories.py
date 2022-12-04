max_cal = 0

with open('calories.txt') as f:
    elf_cal = 0
    for line in f.readlines():
        if line != "\n":
            elf_cal += int(line)
        elif max_cal < elf_cal:
            max_cal = elf_cal
            elf_cal = 0
        else:
            elf_cal = 0
print(f'Maximum calories carried by an elf is: {max_cal}')
# print(f'Maximum calories carried by an elf is: 71924')