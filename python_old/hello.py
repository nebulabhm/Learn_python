try:
    data = open('baa.txt')
    for each_line in data:
        # if (not each_line.find('.') == -1):
        try:
            (role, line_spoken) = each_line.split('.', 1)
            print(role, end='')
            print(' --- ', end='')
            print(line_spoken, end='')
        except:
            pass
    data.close()
except:
    print('The datafile is missing!')