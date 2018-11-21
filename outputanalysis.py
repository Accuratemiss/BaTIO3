def grab_total_energy(path):
    data = open(path, 'r').read()
    position = data.find('Total lattice energy')
    skip_to_data = 34
    data_start = position + skip_to_data
    data_end = data.find(' ',data_start)
    string = data[data_start:data_end]
    if string[0] != '-':
        print ('Non negative total energy, Be careful!!')


    return string
path = 'output1.gout'
grab_total_energy(path)
