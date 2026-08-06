# Skill Matcher

my_skills = {
    "Python",
    "SQL",
    "Git",
    "Machine Learning"
}

job_requirements = {
    "Python",
    "SQL",
    "Docker",
    "Git",
    "AWS"
}

print("My Skills")
print(my_skills)

print()

print("Job Requirements")
print(job_requirements)

print()

print("Matching Skills")
print(my_skills & job_requirements)

print()

print("Skills I Need To Learn")
print(job_requirements - my_skills)

print()

print("All Skills")
print(my_skills | job_requirements)