def grab_total_energy(path):
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
        string.append(new_string)
        position = data_end
        position = data.find(test_find, data_end)
        print(position)


    return string
path = 'output1.gout'

def grab_last_total_energy(path):
    return grab_total_energy(path)[3]

print(grab_last_total_energy(path))
