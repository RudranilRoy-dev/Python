import pickle 
with open("48. file.dat",'rb') as input_file:
    data=pickle.load(input_file)
    for name,marks in data.items():
        if marks>80:
            print(f"Name:{name}, Marks:{marks}")