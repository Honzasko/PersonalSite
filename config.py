server_port = ''


def load_Config(file):
    f = open(file,"r")
    data = f.readlines()
    for line in data:
        line = line.split("=")
        print(line)
        if line[0] == "port":
            server_port = line[1]
