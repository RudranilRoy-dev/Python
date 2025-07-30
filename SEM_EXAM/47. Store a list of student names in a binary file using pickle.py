import pickle
students = ["Riya", "Amit", "Nilu", "Soham", "Priya"]
with open("47. file.dat",'wb') as output_file:
    pickle.dump(students,output_file)