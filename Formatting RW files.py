# Reading write file and writing the bytes in readable formate in new file
location = "Test2\\"

write_files = ["test2 128 1000 Write", "test2 128 2000 Write", "test2 256 1000 Write", "test2 256 2000 Write"]
dic = {b'\x80': '80', b'\x81': '81', b'\x82': '82', b'\xf9': 'f9', b'\xfa': 'fa', b'\xfb': 'fb',
       b'\xfc': 'fc', b'\xfd': 'fd', b'\xfe': 'fe'}
b_arg = {b'\xf9': 5, b'\xfa': 4, b'\xfb': 2, b'\xfc': 5, b'\xfd': 4, b'\xfe': 4}

# Reading write file and writing the bytes in readable formate in new file
for rfile in write_files:
    line = []
    newline = True
    with open(location + rfile + ".txt", 'rb') as file_r:
        with open(location + rfile + " Formatted.txt", 'w') as file_w:
            data = file_r.read()
            b_array = iter([data[i:i+1] for i in range(len(data))])
            for b in b_array:
                if newline:
                    file_w.writelines(''.join(line).strip(' '))
                    line = []
                if newline and b in [b'\x80', b'\x81', b'\x82']:
                    line.extend([dic[b], ' '])
                    newline = False
                    continue
                if b == b'\r':
                    line.append('\n')
                    newline = True
                    continue
                if b in [b'\xf9', b'\xfa', b'\xfb', b'\xfc', b'\xfd', b'\xfe']:
                    line.extend([dic[b], ' '])
                    for k in range(b_arg[b]):
                        pb = next(b_array)
                        line.append(bytes.hex(pb) + ' ')
                    line.append('\n')
                    newline = True
                    continue
                line.append(b.decode('ASCII'))
    print('Done for file: ', rfile + ".txt")

read_files = ["test2 128 1000 Read", "test2 128 2000 Read", "test2 256 1000 Read", "test2 256 2000 Read"]
# Reading read file and writing the bytes in readable formate in new file

for rfile in read_files:
    line = []
    newline = True
    with open(location + rfile + ".txt", 'rb') as file_r:
        with open(location + rfile + " Formatted.txt", 'w') as file_w:
            data = file_r.read()
            b_array = iter([data[i:i+1] for i in range(len(data))])
            for b in b_array:
                if newline:
                    file_w.writelines(''.join(line).strip(' '))
                    line = []
                if newline and b in [b'\x80', b'\x81', b'\x82']:
                    line.extend([dic[b], ' '])
                    newline = False
                    continue
                if b == b'\r':
                    line.append('\n')
                    newline = True
                    continue
                if b in [b'\xf9', b'\xfa', b'\xfb', b'\xfc', b'\xfd', b'\xfe']:
                    line.extend([dic[b], ' '])
                    for k in range(b_arg[b]):
                        pb = next(b_array)
                        line.append(bytes.hex(pb) + ' ')
                    line.append('\n')
                    newline = True
                    continue
                line.append(b.decode('ASCII'))
    print('Done for file: ', rfile + ".txt")

print("Formatting completed!")
