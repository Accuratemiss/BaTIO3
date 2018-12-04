import os
import numpy as np
def grab_total_list(path):
    data = open(path, 'r').read()
    skip_to_data = 34
    position = 0
    string = []
    test_find = 'Total lattice energy'
    position = data.find(test_find)

    while position != -1:
        data_start = data.find('-', position)
        data_end = data.find(' ',data_start)
        new_string = data[data_start:data_end]
        string.append(float(new_string))
        position = data_end
        position = data.find(test_find, data_end)
    return string
path = 'output1.gout'
def grab_total_energy(path):
    #pulls out everything
    return grab_total_list(path)[3]

errorcount = 0

def list_from_folder(folder_path):
    curr_path = os.getcwd()
    os.chdir(curr_path+'\\'+folder_path)
    file_list = os.listdir()
    global errorcount
    out = [['filename', 'Energy']]
    for file in file_list:
        if file[-5:] == '.gout':
            try:
                out_list = [file, str(grab_total_energy(file))]
                out.append(out_list)
                print('Read: ' + file)
            except:
                print('There was a problem with: ' + file)
                errorcount += 1
        else:
            print('skipped file', file)
            print(file[-5:])
    out = np.array(out)
    return out

list = list_from_folder('test_2')
print('Couldn\'t read ' + str(errorcount) + ' .gout files')
np.savetxt('output.csv',np.array(list), fmt = '%s')
