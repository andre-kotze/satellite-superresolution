'''
script will read data from these dirs and delete so many files that only 940 remains for training, and 100 each for validation and testing:

dataset_2
├── hr_2_4m
│   ├── hr
│   ├── hr_test
│   └── hr_valid
└── lr_0_6m
    ├── lr
    ├── lr_test
    └── lr_valid

"delete" means it will be moved to lixo folder

let's begin
'''

import os
from os import listdir as files_in
from os.path import join
import sys
import random
from shutil import move

#DIRS:
hr = 'hr_2_4m/hr'
lr = 'lr_0_6m/lr'

train = '/'
test = '_test/'
valid = '_valid/'

if not os.path.exists('lixo/'):
    os.makedirs(join('lixo/', hr + train))
    os.makedirs(join('lixo/', hr + test))
    os.makedirs(join('lixo/', hr + valid))
    os.makedirs(join('lixo/', lr + train))
    os.makedirs(join('lixo/', lr + test))
    os.makedirs(join('lixo/', lr + valid))



# conduct checks:
if files_in('hr_2_4m/hr') == files_in('lr_0_6m/lr') and \
    files_in('hr_2_4m/hr_test') == files_in('lr_0_6m/lr_test') and \
    files_in('hr_2_4m/hr_valid') == files_in('lr_0_6m/lr_valid'):
    print('All checks passed')
else:
    print('Datasets do not match, exiting')
    sys.exit(0)

traindata = random.sample(files_in(lr + train),940)
for f in files_in(lr + train):
    if f not in traindata:
        move(lr + train + f,'lixo/' + lr + train + f)
        move(hr + train + f,'lixo/' + hr + train + f)

testdata = random.sample(files_in(lr + test),100)
for f in files_in(lr + test):
    if f not in testdata:
        move(lr + test + f,'lixo/' + lr + test + f)
        move(hr + test + f,'lixo/' + hr + test + f)

validdata = random.sample(files_in(lr + valid),100)
for f in files_in(lr + valid):
    if f not in validdata:
        move(lr + valid + f,'lixo/' + lr + valid + f)
        move(hr + valid + f,'lixo/' + hr + valid + f)