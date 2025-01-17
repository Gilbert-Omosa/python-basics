# -----Student Performance Analysis Example----
# List of dictionaries containing student names and their scores in various subjects

results = [{"name": "Jane Rich", "maths": 55, "english": 67, "chem": 59, "kis": 25, "geo": 13},
           {"name": "Jenette Massey", "maths": 38, "english": 48, "chem": 20, "kis": 28, "geo": 70},
           {"name": "Kelly Galloway", "maths": 64, "english": 72, "chem": 53, "kis": 35, "geo": 100},
           {"name": "Wendy Black", "maths": 22, "english": 45, "chem": 59, "kis": 50, "geo": 96},
           {"name": "Alexa Mathews", "maths": 41, "english": 41, "chem": 40, "kis": 55, "geo": 97},
           {"name": "Talon Fitzpatrick", "maths": 69, "english": 35, "chem": 69, "kis": 43, "geo": 36},
           {"name": "Amaya Baker", "maths": 71, "english": 19, "chem": 58, "kis": 83, "geo": 39},
           {"name": "Camden Hunt", "maths": 26, "english": 41, "chem": 22, "kis": 40, "geo": 42},
           {"name": "Malcolm Oliver", "maths": 46, "english": 12, "chem": 35, "kis": 89, "geo": 30},
           {"name": "Marah Rosa", "maths": 39, "english": 40, "chem": 50, "kis": 82, "geo": 90},
           {"name": "Quintessa Ward", "maths": 63, "english": 78, "chem": 32, "kis": 80, "geo": 88},
           {"name": "Cara Hernandez", "maths": 35, "english": 21, "chem": 12, "kis": 14, "geo": 55},
           {"name": "Fay Whitaker", "maths": 43, "english": 32, "chem": 54, "kis": 62, "geo": 48},
           {"name": "Patricia Rhodes", "maths": 59, "english": 45, "chem": 57, "kis": 84, "geo": 79},
           {"name": "Xantha Flowers", "maths": 48, "english": 67, "chem": 11, "kis": 36, "geo": 93},
           {"name": "Chaney Gonzales", "maths": 24, "english": 24, "chem": 45, "kis": 40, "geo": 24},
           {"name": "Lewis Madden", "maths": 68, "english": 31, "chem": 65, "kis": 61, "geo": 93},
           {"name": "Acton Mckenzie", "maths": 66, "english": 47, "chem": 40, "kis": 58, "geo": 22},
           {"name": "Brielle Grimes", "maths": 53, "english": 12, "chem": 14, "kis": 60, "geo": 19},
           {"name": "Lara Spence", "maths": 17, "english": 77, "chem": 15, "kis": 39, "geo": 36},
           {"name": "Lee Rowe", "maths": 21, "english": 10, "chem": 35, "kis": 28, "geo": 95},
           {"name": "Sonia Ford", "maths": 19, "english": 43, "chem": 31, "kis": 76, "geo": 21},
           {"name": "Keelie Cortez", "maths": 51, "english": 89, "chem": 33, "kis": 37, "geo": 92},
           {"name": "Dean Briggs", "maths": 31, "english": 56, "chem": 37, "kis": 55, "geo": 64},
           {"name": "Aristotle Lucas", "maths": 67, "english": 73, "chem": 37, "kis": 56, "geo": 27},
           {"name": "Shelley Clark", "maths": 54, "english": 73, "chem": 35, "kis": 83, "geo": 76},
           {"name": "Lars Pearson", "maths": 20, "english": 17, "chem": 19, "kis": 57, "geo": 55},
           {"name": "Charlotte Dunn", "maths": 21, "english": 26, "chem": 32, "kis": 67, "geo": 17},
           {"name": "Rhonda Green", "maths": 34, "english": 54, "chem": 57, "kis": 79, "geo": 92},
           {"name": "Hamish Peterson", "maths": 30, "english": 18, "chem": 32, "kis": 16, "geo": 22},
           {"name": "Sade Sexton", "maths": 31, "english": 79, "chem": 54, "kis": 50, "geo": 39},
           {"name": "Beverly Sexton", "maths": 67, "english": 13, "chem": 27, "kis": 80, "geo": 23},
           {"name": "Cheyenne Wooten", "maths": 25, "english": 80, "chem": 12, "kis": 27, "geo": 93},
           {"name": "John Henry", "maths": 22, "english": 24, "chem": 66, "kis": 87, "geo": 18},
           {"name": "Ian Suarez", "maths": 14, "english": 13, "chem": 51, "kis": 11, "geo": 92},
           {"name": "Shad Wheeler", "maths": 17, "english": 50, "chem": 65, "kis": 62, "geo": 45},
           {"name": "Chaney Chapman", "maths": 67, "english": 18, "chem": 12, "kis": 49, "geo": 16},
           {"name": "Demetria Abbott", "maths": 42, "english": 30, "chem": 16, "kis": 28, "geo": 42},
           {"name": "Maryam Erickson", "maths": 50, "english": 30, "chem": 60, "kis": 24, "geo": 20},
           {"name": "Clio Mendoza", "maths": 27, "english": 42, "chem": 28, "kis": 29, "geo": 30},
           {"name": "Anastasia Pratt", "maths": 50, "english": 58, "chem": 49, "kis": 19, "geo": 47},
           {"name": "Cally Perkins", "maths": 31, "english": 67, "chem": 66, "kis": 13, "geo": 38},
           {"name": "Coby Dodson", "maths": 55, "english": 28, "chem": 19, "kis": 86, "geo": 58},
           {"name": "Phoebe Byrd", "maths": 32, "english": 85, "chem": 40, "kis": 16, "geo": 36},
           {"name": "Sonia Wiggins", "maths": 30, "english": 58, "chem": 68, "kis": 40, "geo": 36},
           {"name": "Olympia Velasquez", "maths": 32, "english": 33, "chem": 44, "kis": 62, "geo": 48},
           {"name": "Caesar Hodge", "maths": 71, "english": 59, "chem": 25, "kis": 71, "geo": 60},
           {"name": "Alisa Shepard", "maths": 79, "english": 63, "chem": 30, "kis": 90, "geo": 34},
           {"name": "Yardley Carver", "maths": 62, "english": 24, "chem": 37, "kis": 52, "geo": 95},
           {"name": "Camille Faulkner", "maths": 24, "english": 29, "chem": 48, "kis": 49, "geo": 28},
           {"name": "Cally Fisher", "maths": 13, "english": 15, "chem": 67, "kis": 11, "geo": 14},
           {"name": "Francesca Bauer", "maths": 13, "english": 38, "chem": 26, "kis": 60, "geo": 61},
           {"name": "Otto Buchanan", "maths": 49, "english": 23, "chem": 64, "kis": 66, "geo": 63},
           {"name": "Emily Phelps", "maths": 60, "english": 14, "chem": 33, "kis": 56, "geo": 81},
           {"name": "Chelsea Beasley", "maths": 17, "english": 59, "chem": 20, "kis": 78, "geo": 17},
           {"name": "Kelsey Wolf", "maths": 75, "english": 34, "chem": 61, "kis": 90, "geo": 76},
           {"name": "Caryn Hays", "maths": 12, "english": 73, "chem": 33, "kis": 12, "geo": 76},
           {"name": "Whilemina Glenn", "maths": 29, "english": 80, "chem": 66, "kis": 40, "geo": 73},
           {"name": "Ali Reynolds", "maths": 79, "english": 64, "chem": 57, "kis": 71, "geo": 45},
           {"name": "Abbot Salazar", "maths": 25, "english": 42, "chem": 42, "kis": 60, "geo": 45},
           {"name": "Alika Campos", "maths": 36, "english": 54, "chem": 57, "kis": 17, "geo": 31},
           {"name": "Joshua Mays", "maths": 55, "english": 36, "chem": 69, "kis": 40, "geo": 22},
           {"name": "Aileen Rutledge", "maths": 41, "english": 69, "chem": 32, "kis": 11, "geo": 63},
           {"name": "Allen Trevino", "maths": 13, "english": 18, "chem": 32, "kis": 54, "geo": 46},
           {"name": "Joan Hudson", "maths": 61, "english": 11, "chem": 51, "kis": 59, "geo": 44},
           {"name": "Addison Pate", "maths": 56, "english": 90, "chem": 47, "kis": 27, "geo": 36},
           {"name": "Dominic Hancock", "maths": 65, "english": 43, "chem": 51, "kis": 73, "geo": 80},
           {"name": "Indira Harding", "maths": 24, "english": 50, "chem": 25, "kis": 21, "geo": 25},
           {"name": "Hyacinth Frye", "maths": 29, "english": 24, "chem": 62, "kis": 61, "geo": 13},
           {"name": "Mannix Lawrence", "maths": 22, "english": 15, "chem": 29, "kis": 80, "geo": 81},
           {"name": "Hayley Foster", "maths": 48, "english": 18, "chem": 28, "kis": 15, "geo": 25},
           {"name": "Elvis Ross", "maths": 40, "english": 89, "chem": 45, "kis": 34, "geo": 83},
           {"name": "Zane Dixon", "maths": 18, "english": 60, "chem": 26, "kis": 27, "geo": 39},
           {"name": "Micah Frank", "maths": 18, "english": 24, "chem": 67, "kis": 69, "geo": 82},
           {"name": "Iris Reynolds", "maths": 49, "english": 43, "chem": 21, "kis": 19, "geo": 29},
           {"name": "Ferris Chandler", "maths": 11, "english": 83, "chem": 35, "kis": 77, "geo": 16},
           {"name": "Herman Wilcox", "maths": 22, "english": 27, "chem": 30, "kis": 73, "geo": 99},
           {"name": "Alfonso Booth", "maths": 70, "english": 24, "chem": 13, "kis": 28, "geo": 11},
           {"name": "Jaime Wilkerson", "maths": 61, "english": 38, "chem": 62, "kis": 76, "geo": 13},
           {"name": "Ingrid Conner", "maths": 37, "english": 25, "chem": 33, "kis": 19, "geo": 14},
           {"name": "Kennan Grant", "maths": 53, "english": 16, "chem": 49, "kis": 87, "geo": 78},
           {"name": "Herrod Medina", "maths": 36, "english": 12, "chem": 50, "kis": 44, "geo": 36},
           {"name": "Elizabeth Hudson", "maths": 49, "english": 81, "chem": 38, "kis": 71, "geo": 85},
           {"name": "Russell Dotson", "maths": 10, "english": 12, "chem": 16, "kis": 80, "geo": 20},
           {"name": "Zephania Kemp", "maths": 64, "english": 81, "chem": 62, "kis": 80, "geo": 51},
           {"name": "Malcolm Roman", "maths": 46, "english": 85, "chem": 24, "kis": 72, "geo": 55},
           {"name": "Ahmed Perkins", "maths": 54, "english": 54, "chem": 41, "kis": 22, "geo": 14},
           {"name": "Dylan Jenkins", "maths": 73, "english": 51, "chem": 60, "kis": 56, "geo": 19},
           {"name": "Rigel Mcguire", "maths": 26, "english": 70, "chem": 31, "kis": 75, "geo": 83},
           {"name": "Evan Reeves", "maths": 70, "english": 77, "chem": 34, "kis": 21, "geo": 24},
           {"name": "Vance Sheppard", "maths": 66, "english": 71, "chem": 29, "kis": 19, "geo": 83},
           {"name": "Orlando House", "maths": 13, "english": 80, "chem": 43, "kis": 80, "geo": 80},
           {"name": "Maryam Garner", "maths": 13, "english": 78, "chem": 53, "kis": 44, "geo": 11},
           {"name": "Garrett Walton", "maths": 16, "english": 82, "chem": 24, "kis": 38, "geo": 48},
           {"name": "Maggie Buckner", "maths": 37, "english": 79, "chem": 58, "kis": 82, "geo": 21},
           {"name": "Joy Dillon", "maths": 15, "english": 34, "chem": 18, "kis": 66, "geo": 79},
           {"name": "Ian Tyler", "maths": 40, "english": 21, "chem": 34, "kis": 37, "geo": 12},
           {"name": "Quinlan Palmer", "maths": 22, "english": 58, "chem": 16, "kis": 12, "geo": 59},
           {"name": "Myra Delaney", "maths": 13, "english": 64, "chem": 63, "kis": 63, "geo": 32},
           {"name": "Linus Adkins", "maths": 69, "english": 18, "chem": 68, "kis": 31, "geo": 49}]

# Count the number of students
print(f"Total Number of students: {len(results)}")

# Calculate total scores for each student and sort by total score
for result in results:
    total = result["maths"] + result["english"] + result["chem"] + result["kis"] + result["geo"]
    result["total"] = total

results = sorted(results, key=lambda k: k["total"], reverse=True)

# Print the top student overall based on total scores
print(f"\nTop overall student: {results[0]['name']} with a total of {results[0]['total']} marks.")

# Top 10 overall (sorted by total score in descending order)
top_10_overall = sorted(results, key=lambda r: r["total"], reverse=True)[:10]
print("\nTop 10 Overall:")
for student in top_10_overall:
    print(f"{student['name']} - Total: {student['total']}")

# Top student in math
results = sorted(results, key=lambda k: k["maths"], reverse=True)
print(f"\nTop student in Mathematics: {results[0]['name']} with {results[0]['maths']} marks.")

# Top student in english
results = sorted(results, key=lambda k: k["english"], reverse=True)
print(f"Top student in English: {results[0]['name']} with {results[0]['english']} marks.")

# Top student in chemistry
results = sorted(results, key=lambda k: k["chem"], reverse=True)
print(f"Top student in Chemistry: {results[0]['name']} with {results[0]['chem']} marks.")

# Top student in kiswahili
results = sorted(results, key=lambda k: k["kis"], reverse=True)
print(f"Top student in Kiswahili: {results[0]['name']} with {results[0]['kis']} marks.")

# Top student in geography
results = sorted(results, key=lambda k: k["geo"], reverse=True)
print(f"Top student in Geography: {results[0]['name']} with {results[0]['geo']} marks.")

# Total Mean score
total_mean_score = sum(r["total"] for r in results) / len(results)
print(f"\nTotal Mean score: {total_mean_score}")

# Mean score in Mathematics
math_mean_score = sum(r["maths"] for r in results) / len(results)
print(f"\nMean score in Mathematics: {math_mean_score}")

# Mean score in English
eng_mean_score = sum(r["english"] for r in results) / len(results)
print(f"Mean score in English: {eng_mean_score}")

# Mean score in Chemistry
chem_mean_score = sum(r["chem"] for r in results) / len(results)
print(f"Mean score in Chemistry: {chem_mean_score}")

# Mean score in Kiswahili
kis_mean_score = sum(r["kis"] for r in results) / len(results)
print(f"Mean score in Kiswahili: {kis_mean_score}")

# Mean score in Geography
geo_mean_score = sum(r["geo"] for r in results) / len(results)
print(f"Mean score in Geography: {geo_mean_score}")
