def read_data(filename):
    # Resource leak: file is opened but never closed
    f = open(filename, 'r')
    return f.read()

unused_temp = "unused"
