# Mad Libs Game - Karachi Girl's Inspiring Journey

print("🌟 Welcome to the Mad Libs Game: Karachi Girl's Story 🌟\n")
print("="*50 )

# User Inputs
girl_name = input("Enter the girl's name: ")
exam_name = input("Enter the exam she passed (e.g. CSS, PPSC, SPSC): ")
school_type = input("Enter the school type where she got her first job (e.g. government school, private school): ")
company_name = input("Enter the name of a multinational company she worked in: ")
it_course = input("Enter the IT course she is learning (e.g. Web Development, Python, Data Science): ")

# The Story
story = f"""
There is a girl named {girl_name} who lives in Karachi. She is the pride of her parents.
By the grace of Almighty Allah, she passed her {exam_name} exam in the government sector and 
found a job as a teacher in a {school_type}. After a few years of dedication and hard work, 
she was promoted to the position of Headmistress.

Her journey didn't stop there. She also became a part of a multinational company named {company_name},
where she served as an HR Manager as well as an Accounts Manager.

Nowadays, she is learning {it_course} to upgrade her skills and is hopeful for the best.
Her life is a true example of hard work, faith, and perseverance.
"""

# Print the final story
# print("\n📝 Here's the story you created:\n")
print(story)
