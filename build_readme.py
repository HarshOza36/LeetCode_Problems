import os
import re
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input pdf folder")
args = vars(ap.parse_args())

# all inputs
readme = "README.md"
# folder = "String\\"
folder = args['input']


files = os.listdir(folder)
files.remove(readme)
readme = folder+readme

# getting only problem numbers as file names in the folder
for i in range(len(files)):
    files_temp, _ = files[i].split("-")
    files_temp = files_temp[1:-1]
    files[i] = files_temp
files.sort()
files.sort(key=len)
print(f"Input Folder File numbers : {files}")

# Read readme.md
with open(readme, "r") as f:
    readme_content = f.readlines()
    f.close()


# Get new files
regex = re.compile(r'[0-9]')
for ids, sentence in enumerate(readme_content):
    if(sentence[0] == "|" and regex.match(sentence[1]) != None):
        problem_no = sentence.split(".")[0][1:]
        if(problem_no in files):
            files.remove(problem_no)
print(f"New File numbers : {files}")


# Creating new readme content
new_readme_content = []
# for ids, sentence in enumerate(readme_content):
ids = 0
while ids < len(readme_content):
    sentence = readme_content[ids]
    if(sentence[0] == "|" and regex.match(sentence[1]) != None):
        problem_no = sentence.split(".")[0][1:]
        if(files and int(problem_no) > int(files[0])):
            index_of_problem = ids
            new_readme_content.append(f"|{files[0]}. []()|[Solution]()|\n")
            
            files.remove(files[0])
            # still re checking the curr problem_no > new files[0]
            # if yes, we will stay on same id
            if(files and int(problem_no) > int(files[0])):
                ids -= 1
                # because in main loop we will do ids += 1 
            else:
                # only append line when we are more than the numbers
                new_readme_content.append(sentence)
        else:
           # just append the line if we didnt reach the number
           new_readme_content.append(sentence)
    else:
        # Then it is headers, or empty lines
        new_readme_content.append(sentence)
    ids += 1

if(len(files) != 0):
    for i in files:
        new_readme_content.append(f"|{i}. []()|[Solution]()|\n")


# Writing out to the original file.
with open(readme, "w") as out:
    for i in new_readme_content:
        out.write(i)
    out.close()

print("<<< New Readme Created Successfully >>>")
