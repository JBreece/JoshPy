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


# problem 4 Rabbits and Recurrence Relations
print('\nproblem 4')

n = 5 # changing this to the default from the problem, since it requires a lot of cpu time to calculate this
k = 3
p = 1

def bunnies(n):
    if(n > 1):
        p = bunnies(n-1) + (bunnies(n-2) * k)
        # note here, the struggle with this one was figuring out that because you have to go 2 generations back (because the bunnies need 1 generation to grow into maturity to be able to reproduce) then you actually need to have 2 base cases, not just 1.  Something to keep in mind for future recursion problems, if you have to go multiple "generations" (function calls) backwards (as in, function(n-2) or function(n-3) you'll need that many base cases.  So needed the below 2 base cases:
    elif(n == 1):
        p = 1
    else:
        p = 0
    return p

print(bunnies(n))
# lesson learned here, for any recursive function f(n), you'll need x number of base cases where x is the number of previous steps you take backwards in the recursive function, such as f(n-x)
    # in the above example, f(n-x) is bunnies(n-2), so x = 2.  2 base cases required.


# problem 5 Mortal Fibonacci Rabbits
print('\nproblem 5')

p = 1
n = 6
m = 3
k = 1 # could just leave this out, but in the spirit of keeping consistency with the bunny problems, "k" is just 1 for this problem (mature rabbit pairs only produce 1 offspring when they reproduce)
def bunnies_mortal(n):
    if(n > 1):
        p = bunnies_mortal(n-1) + (bunnies_mortal(n-2) * k) - bunnies_mortal(n-(m+1))
        #print(p)
    elif(n == 1):
        p = 1
    else:
        p = 0
    return p

#bunnies_mortal(n)
print(bunnies_mortal(n))

# can't figure out why my solution is not working.  There's a problem conceptually with what I'm doing where my code can't "remember" when it's already killed off a bunny, but that should be giving me less bunnies than the solution, not more.  Not sure what's going on.
# this solution from online works, but I'm not sure why or how, and I'm not sure how I should have come to the conclusion to get to this solution (like what logically should have led to this) and there's no good explanation that I can find online.  So next steps I can take a look at this solution and figure out how it works, but for now I'm going to something else.  Rosalind doesn't actually post their suggested solutions/explanations so if you don't have a teacher it's either hope google helps, or give up.  So I'm going to look for a different tutorial site.
def mortal_rabbits(n, m):
    sequence = [1, 1]

    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            #Normal fibonacci - No deaths yet
            new_num = sequence[i] + sequence[i + 1]
        else:
            #Different reoccurence relation - Accounting for death
            for j in range(m - 1):
                new_num += sequence[i - j]

        sequence.append(new_num)

    return sequence

print(mortal_rabbits(n, m))