import pickle
dict={"nil":90,"rudra":88,"roy":40}
with open("48. file.dat",'ab') as output_file:
    pickle.dump(dict,output_file)