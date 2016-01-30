import pickle

def dump_picle(data, filename, protocol=None):
    pickle.dump(data, open(filename, "wb"), protocol=protocol)  # protocol =4 for large file >= 4GB
    print('Pikle file has been saved in %s.'%filename)