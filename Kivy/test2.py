
file1 = open('file1.html', 'r')
file2 = open('file2.html', 'r')

for line1 in file1:
    line2 = file2.readline()
    if line1 == line2:
        continue
    else:
        print('Line1: {}\nLine2: {}'.format(line1, line2))


file1.close()
file2.close()
