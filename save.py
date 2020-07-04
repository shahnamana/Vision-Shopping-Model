import pandas as pd
file_path = pd.read_csv(r'styles.csv')

l = []

for i in range(len(file_path)):
    if file_path['articleType'][i] == 'Dresses' or file_path['articleType'][i] == 'Kurtis':
        l.append(file_path['id'][i])


import shutil
from pathlib import Path


for i in range(len(l)):
    src = 'images/' + str(l[i])+'.jpg'
    dst = 'dresses/'+str(l[i])+'.jpg'
    my_file = Path(src)
    if my_file.exists():
        shutil.copyfile(src, dst)
    else:
        continue
print(len(l))
print("successful")