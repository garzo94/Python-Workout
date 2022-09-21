def get_final_line(file):
    last_line = ''
    with open(file) as f:
        for line in f:
           last_line = line
    print(line)

get_final_line('fakefile.txt')