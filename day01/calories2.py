max_cal1 = 0
max_cal2 = 0
max_cal3 = 0

with open('calories.txt') as f:
    elf_cal = 0
    for line in f.readlines():
        if line != "\n":
            elf_cal += int(line)
        elif max_cal1 < elf_cal:
            max_cal3 = max_cal2
            max_cal2 = max_cal1
            max_cal1 = elf_cal
            elf_cal = 0
        elif max_cal2 < elf_cal:
            max_cal3 = max_cal2
            max_cal2 = elf_cal
            elf_cal = 0
        elif max_cal3 < elf_cal:
            max_cal3 = elf_cal
            elf_cal = 0
        else:
            elf_cal = 0
print(f'Maximum calories carried by an elf is: {max_cal1}')
print(f'Second maximum calories carried by an elf is: {max_cal2}')
print(f'Third maximum calories carried by an elf is: {max_cal3}')
print(f'Total carried by these 3: {max_cal1 + max_cal2 + max_cal3}')
# print(f'Maximum calories carried by an elf is: 71924')