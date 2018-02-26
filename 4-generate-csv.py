from os import listdir
from os.path import isfile, join


samples = ['./training-set-anton/']
outfile = 'training-data.csv'

f = open(outfile, 'w')

count = 0
for mypath in samples:

    onlyfiles = [mypath + f for f in listdir(mypath)
                 if isfile(join(mypath, f))]
    
    for fp in onlyfiles:
        f.write('{};{}\n'.format(fp, count))

    count += 1

f.close()
    
