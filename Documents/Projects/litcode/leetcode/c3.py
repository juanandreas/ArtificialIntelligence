import re

# read the string filename
filename = input()

print("i hate hackerrank")
fil = open(filename, "r")

C = []
CPP = []
CS = []

for line in fil:
    if re.match(r".*\.c$", line):
        C.append(line)
    if re.match(r".*\.cpp$", line):
        CPP.append(line)
    if re.match(r".*\.cs$", line):
        CS.append(line)

print(C)
print(CPP)
print(CS)

file_nm = filename.split(".")[0]
C_files = open("c_{}".format(file_nm), "w+")
CPP_files = open("cpp_{}".format(file_nm), "w+")
CS_files = open("cs_{}".format(file_nm), "w+")

for c_file in C:
    C_files.write(c_file)

for cpp_file in CPP:
    CPP_files.write(cpp_file)

for cs_file in CS:
    CS_files.write(cs_file)