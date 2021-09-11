# Rosalind problems (rosalind.info)





# Python Village problems:





# problem 2 Variables and Some Arithmetic (problem 1 is installing python)
print('problem 2')

a = 976
b = 842
c = (a*a) + (b*b)
print(c)


# problem 3 Strings and Lists
print('\nproblem 3')

s = 'Ar962GjJpC4yWqm7eqgXf2G1EE9kKh1dqy1cjUZyewBWWParaphysaa7OcSWndIVsiEjotVbedriagaiLvXr4B0DFsUYGWRjyPlBkYLhKjwg7M3UT2AdjFC5QBgJ2uQRdlu7RO2bWiVyPtrOm6qXqDGucXUiVkurGIsTuGD2.'
a = 45
b = 53
c = 71
d = 79
print(s[a:(b+1)], s[c:(d+1)])


# problem 4 Conditions and Loops
print('\nproblem 4')

a = 4270
b = 8848
sum = 0
for i in range(a, b):
    if (i%2) == 1:
        sum = sum + i
print(sum)


# problem 5 Working with Files
print('\nproblem 5')

# input and clean file first (removing newlines):
f = open('input.txt', 'r')
lines = f.readlines()
lines_clean = []
for line in lines:
    lines_clean.append(line.strip('\n'))
# then output:
numLines = 0
f = open('output.txt', 'w')
for line in lines_clean:
    numLines += 1
for i in range(numLines):
    i += 1
    if(i%2) == 0:
        f.write(lines_clean[(i-1)] + '\n')
        # just realized the .write function would not add newlines... so cleaning was totally unnecessary.
        # :(


## alternative method (minus line cleaning for \n):
#with open('input.txt', 'r') as f:
#    lines = f.readlines()
#    numLines = 0
#    f = open('output.txt', 'w')
#    for line in lines:
#        numLines += 1
#    for i in range(numLines):
#        i += 1
#        if(i%2) == 0:
#            f.write(lines[(i-1)])


# problem 6 Dictionaries
print('\nproblem 6')

s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
d = {}
list = s.split()
for word in list:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
for key, value in d.items():
    print(key, value)





# Bioinformatics Stronghold problems:





# problem 1 Counting DNA Nucleotides
print('\nproblem 1')

s = 'GCATTTTAAGCTAGGAGAGCCCGACGTTATGCGTACGGCATGGTAACCGTGGGTCGCCTGAATTGTGCTATGCTTCCCACTGTCCAAGGTTTATACATTTTATAAGACTCTCAGGCTTAAAACAGAACAGTTCCCCCCATGTGGCTATGATAAACCAGAGGAGAGCTACGACTCACATCTTTCCGCGGGGTCAAGTGGCCTTCCGGCACGACCTTAAAAAAGTTGTATGGTGCTACACAGAGACACCAATAAGCACATTCGGCCATCTTTTACCTCGTGCAAACCCAAGCACAATTACAGCGTTACCATATGGTCAGCTTTGTAGGCCGCCGAGTAATAACGTTCCACATGTCCGGAAATTTCTCAGCCGACGGATGCTGGCTCTGTTACCCCTTGCGCACAGGGTAGATTGTATGGAAGCCTGGTTGACATTGATAGGATGGATTGAGTACTCCGACTCATTTGTCGGGAAATGGCCAAACCTGGACAATAGAACCTAAGGCATCAAAATTTACATATACATGCGACCCCGCCTTTGGTGCTCACCACAGCTTTTGACGGGTTCAGCGAACGTTCACATACTTTACTCTCGCACGGTGTAGCGTGCCTCATGACAATAATCACCAAGATGGTATGGGTGGCGTGGGATCCCGTTTGGGCTTCTAATGATTTGAACATTGGTTAAGAGCCTCCTTTCGAGACGCTTTGTCTTGCGCACAGATTGAATGCAGGTACAGGATGAGACCCGAAGAATAACGCAGAGCACAGGTCGTGTGTTACCAGACGAGCTGAACTCGTTAGTTCTCGCTACACGTACCCTTCGTTCTACCCTCTGCGACGACCGAAGGATGATAGTATCCTTCGAGATCTAGGCCAGTTTATTTGGCGCTCCGGCGCCAAACGCGTGGTGAACTGCTTTACTGAGTTCAGTCATCATGAGGCTCGAATTGTACGGAGAGCCTTGGATCACGGGGATAAAACATCGGCGATAGTGAGAAGT'
A = 0
C = 0
G = 0
T = 0
for x in s:
    if(x == 'A'):
        A += 1
    elif(x == 'C'):
        C += 1
    elif(x == 'G'):
        G += 1
    elif(x == 'T'):
        T += 1
print(A, C, G, T)


# problem 2 Transcribing DNA into RNA
print('\nproblem 2')

dna = 'GATCTGTATCTTGCATGAGTGCAATTCGGTAATGTAATCTGGTACTACCCGAAGGCCTTCTTATACAACTACAGAGCCATGGTGATTCCGCTAAACACTTAATACTAGGCAAGCTGTGGGCTATAATAACCCGCGGACGCACTCTGGTTGTGCGACTACGTGCACTTATGATTTCCACGACGCTTGTGGGCTTTTAGGAACAAACTATCCGAACCACAAATTGTGTCACCCGCTTCGCCTCTGATCATTACCTCCAATTAGATGCGCGAGTCTGAGACGACTGCACCGAACCTAATTTTGAGGCGTTACGCCTGGGATACGTGGGAGGTGGCGCCGACCAAGGATTCACATCATGAACCACGGTGGGCTATACAATTTCAACACCTTTTATGTTCGTAAGGAATGGGAATATACACATTGAGCGACTATCCGGGGGAGCCTAGGGTGGCTAGTCTCAGTGGCCAGTCATACAACCATCAGCACCAAGTAGTTTTCAGATGTGAGCCGTTGTGGCCGGTCTGATATCGTGTCTCAACCTAGGAATCATAGGAGCAAGATTATTAAAAATTGGTCAAAGGAGAATAGACGAAGGGCCCGGTGATACGGGGTCGACAATGCCTTACAATTGGAGTACATGCCGCGTACCGGGAATTGGGTTACGCACCATGAACCTACATTGATTGTCGACTGACGGTTCAGGTGGGCCTCGAGCCTCAATATGTGTCATGAGGAGGGGGCCCAGATTCCTTAGCCCCCTCCCTGATGTAACCCGTACTTTTCTCGACTATAGACCAACGCCGAATCTCAATCGCGCGAAGTGCGAAGCACATCCGGGTTCCTTTCTGTGATACAGGCGTTATTTACTAAAGACCTTTCACAAAATTCGGATGCGCCGAGCCGCTCTATGGCCTTGTTGGCTGTGTATGGGCTTCAGGGTTTGCAACTAAGCTGCGGATGGCCCTTGA'
rna = dna.replace("T", "U")
print(rna)


# problem 3 Complementing a Strand of DNA
print('\nproblem 3')

dna = 'TCCTCGCTAATCATTACGTGGGAGCCGCTTATAACACTCGCGGATCGTGTAATGGGAAGTTTGCACGAGCTTGCAGGGTAATTGGAAGCATAGACGGGTTTCTCCGGACCCCATATCTGGAGGCACGTCTTGTATATCACGTCCAACGATAGGGAGACTGCTAGAGACAAGCAAAGGAGATAGAGCAGGTATTGGATCTCGACAAAAAAGGACGTCTTGATCTTAATCGCCTTTCCATTGCGTGAGTAAAGCCAGAAGCATGGCTATAGGAACCATCGATAGTCGCCCAGCGAATCCAGAGGTGATGCGTCATACACAAGGCAACCTCGGGCTCGCTGAGAGGGGTGAGGCTTGCGCCCAGCAGATATTCCACGCGGATCACTTACGCCATTTGCGGATGCATGTTACCCACAGGTGCAGTGGTCTGTACCACGTGAAGCCATGTAGGTGGCAAAGACAATATATAGTGAGTGTAAGCAACGTACCGGACTTGAAAGGTCATTTTCCAATCAACGTGAAGAACACCATCCACATGTTAGTTGGGATGCCGAGTCGCTCACAAGCCAGTGCTCTTCGCTGTGGAATTAGATTTTAACACCTCGAAATGATAACGACACATTAGGACAGTTGCATAAGATTGACTGTGAAAATCTCATATAGCAATCAACCTTAAGGTGAGTCGTTGGGGTACGAGTCCAGATACGGAGACTAGGCAGTTCTACCGGATATCGGATCTCTCAGCACTCCGGCAAGAACGCTATTTAACACGGCTGAGCGATCGACGATGATGGGCCTATCTGGGATGACGAATGATTATTACAATAAATTAACCCGGAACATAGGTCCGGAATTGCCCGGTGCTGTCGCTACATTCATAAGTTTGTTATCGCCACAACTTCTCTGCTATTCGTAAATATTTACCCTAACAACACCAAGACGATCACTGCTATGAGTTGGGGTT'
# print(dna)
# would do .replace() here as well but then it'd require an intermediary variable for each A/T and C/G.  This seems more straight forward:
for index, x in enumerate(dna):
    if(x == "A"):
        dna = dna[:index] + "T" + dna[index + 1:]
    elif(x == "T"):
        dna = dna[:index] + "A" + dna[index + 1:]
    elif(x == "C"):
        dna = dna[:index] + "G" + dna[index + 1:]
    elif(x == "G"):
        dna = dna[:index] + "C" + dna[index + 1:]
reverse_compliment = dna[::-1] # this is the "extended slice" in python - [begin:end:step]
# print(dna)
print(reverse_compliment)