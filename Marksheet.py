Chemistry_theory = int(input("Enter your Chemistry Theory Marks (out of 75): "))
if Chemistry_theory > 0 or Chemistry_theory < 75:
    Chemistry_practical = int(input("Enter your Chemistry Practical Marks (out of 25): "))
    Biology_theory = int(input("Enter your Biology Theory Marks (out of 75): "))
    Biology_practical = int(input("Enter your Biology Practical Marks (out of 25): "))
    Sindhi_Salees = int(input("Enter your Sindhi Salees Marks (out of 75): "))
    English = int(input("Enter your English Marks (out of 75): "))
    Pakistan_Studies = int(input("Enter your Pakistan Studies Marks (out of 50): "))
    Total_marks = (Chemistry_practical+Chemistry_theory+Biology_theory+Biology_practical+Sindhi_Salees+English+Pakistan_Studies)
    percent_chemistry_theory = int(Chemistry_theory/75*100)
    percent_chemistry_practical = int(Chemistry_practical/25*100)
    percent_biology_theory = int(Biology_theory/75*100)
    percent_biology_practical = int(Biology_practical/25*100)
    percent_sindhi_salees = int(Sindhi_Salees/75*100)
    percent_english = int(English/75*100)
    percent_pakistan_studies = int(Pakistan_Studies/75*100)
    percent_total_marks = int(Total_marks/425*100)
    print("Here's your Mark Sheet")
    print("===================================================================")
    print("                          MARK SHEET                         ")
    print("-------------------------------------------------------------------")
    print("|    Subject Name     | Marks Obtained | Total Marks | Percentage |")
    print("|  Chemistry Theory   |        "+str(Chemistry_theory)+"      |      75     |     "+str(percent_chemistry_theory)+"%    |")
    print("| Chemistry Practical |        "+str(Chemistry_practical)+"      |      25     |     "+str(percent_chemistry_practical)+"%    |")
    print("|   Biology Theory    |        "+str(Biology_theory)+"      |      75     |     "+str(percent_biology_theory)+"%    |")
    print("|  Biology Practical  |        "+str(Biology_practical)+"      |      25     |     "+str(percent_biology_practical)+"%    |")
    print("|    Sindhi Salees    |        "+str(Sindhi_Salees)+"      |      75     |     "+str(percent_sindhi_salees)+"%    |")
    print("|       English       |        "+str(English)+"      |      75     |     "+str(percent_english)+"%    |")
    print("|   Pakistan Studies  |        "+str(Pakistan_Studies)+"      |      75     |     "+str(percent_pakistan_studies)+"%    |")
    print("|        Total        |        "+str(Total_marks)+"     |      425    |     "+str(percent_total_marks)+"%    |")
else:
    print('The marks should be between o and 75')