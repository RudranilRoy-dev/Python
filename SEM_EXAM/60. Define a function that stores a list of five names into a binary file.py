import pickle
def store_name(name_list):
    with open("60. file.dat",'wb') as output_file:
        pickle.dump(name_list,output_file)

names=["riya","rudra","nil","roy","nilu"]
store_name(names)
