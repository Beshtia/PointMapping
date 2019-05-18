import pandas as pd
import numpy as np

location = "Test2\\"

write_files = ["test2 128 1000 Write", "test2 128 2000 Write", "test2 256 1000 Write", "test2 256 2000 Write"]
read_files = ["test2 128 1000 Read", "test2 128 2000 Read", "test2 256 1000 Read", "test2 256 2000 Read"]
with pd.ExcelWriter(location + "Points.xlsx") as writer:
    for rfile in write_files:
        x = []
        y = []
        with open(location + rfile + " Formatted.txt", 'r', encoding='ASCII') as file:
            for line in file:

                if line[:5].strip() == '81 fa':
                    b_order = line[6:].strip().split(' ')
                    b_order = ''.join(['0x'] + b_order[::-1])
                    x.append(int(b_order, 0))
                if line[:5].strip() == '82 fa':
                    b_order = line[6:].strip().split(' ')
                    b_order = ''.join(['0x'] + b_order[::-1])
                    y.append(int(b_order, 0))
        y.pop()  # Last point is send twice for finish designation
        x.pop()
        points = np.column_stack((x, y))
        pnt_df = pd.DataFrame(points, columns=['X-axis', 'Y-axis'])
        pnt_df.insert(1, '', points.shape[0]*[''])
        pnt_df.to_excel(writer, sheet_name=rfile, index=False)
        print('Done for file: ', rfile + ".txt")

    for rfile in read_files:
        x = []
        y = []
        znam = False
        with open(location + rfile + " Formatted.txt", 'r', encoding='ASCII') as file:
            for line in iter(file):
                if znam:
                    if line[:10].strip() == '81 RPA':
                        ps = int(next(file))
                        x.append(ps)
                    if line[:10].strip() == '82 RPA':
                        ps = int(next(file))
                        y.append(ps)
                    if line[:22].strip() == '80 fb 00 00':
                        znam = False
                elif line.strip() == '80 G':
                    znam = True
            points = np.column_stack((x, y))
            pnt_df = pd.DataFrame(points, columns=['X-axis', 'Y-axis'])
            pnt_df.insert(1, '', points.shape[0] * [''])
            pnt_df.to_excel(writer, sheet_name=rfile, index=False)
            print('Done for file: ', rfile + ".txt")

print("Creating excel file complete!")
