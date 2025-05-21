def table(n):
    with open (f"tables/table_{n}.txt","w") as file:
        for i in range (1,11):
            y=f"{n} x {i} = {n*i}\n"
            file.write(y)

for i in range (2,21):
    table(i)