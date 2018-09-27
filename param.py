import pickle

shared = {"update":True}

with open('shared.pkl', 'wb') as handle:
    pickle.dump(shared, handle, protocol=pickle.HIGHEST_PROTOCOL)