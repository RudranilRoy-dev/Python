with open("41. file.txt",'r') as input_file:
    vowels={'a','e','i','o','u'}
    lines=input_file.readlines()
    for line in lines:
        vowel_count=0
        consonant_count=0
        for char in line:
            if char.isalpha():
                if char.lower() in vowels:
                    vowel_count+=1
                else:
                    consonant_count+=1
        print(f"{line}")
        print("Vowels:",vowel_count)
        print("Consonants:",consonant_count)