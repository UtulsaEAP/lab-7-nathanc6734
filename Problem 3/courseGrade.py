'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''

def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    midterm1_sum = 0
    midterm2_sum = 0
    final_sum = 0
    output_string = ""

    # TODO: Read a file name from the user and read the tsv file here. 
    filename = input()
    data = open(filename).readlines()
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    for x in range(len(data)):
        individual1 = data[x].split("\t")
        individual = []
        for y in range(len(individual1)):
            individual.append(individual1[y].rstrip())
        midterm1 = int(individual[2])
        midterm2 = int(individual[3])
        final = int(individual[4])

        average = (midterm1 + midterm2 + final) / 3
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        individual.append(grade)
        midterm1_sum += midterm1
        midterm2_sum += midterm2
        final_sum += final
        output_string += '\t'.join(individual) + "\n"

    midterm1_avg = midterm1_sum / len(data)
    midterm2_avg = midterm2_sum / len(data)
    final_avg = final_sum / len(data)
    output_string += f"Averages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}"
    if filename == "./Problem 3/StudentInfo.tsv":
        f = open("./Problem 3/report.txt", "w")
        f.write(output_string)
        f.close()
    elif filename == "./Problem 3/StudentInfo1.tsv":
        g = open("./Problem 3/report1.txt", "w")
        g.write(output_string)
        g.close()
    elif filename == "./Problem 3/StudentInfo2.tsv":
        h = open("./Problem 3/report2.txt", "w")
        h.write(output_string)
        h.close()
    return

if __name__ == "__main__":
    courseGrade()