print("="*25, "WELCOME TO NAUKRI", "="*25)

name = input("Enter your name: ").strip()
address = input("Enter your address: ").strip()
mobile_number = input("Enter your mobile number: ").strip()
email_id = input("Enter your email id: ").strip()

qualification = input(
    "Enter your highest qualification (10th/Diploma/Intermediate/BTech/PhD): "
).strip()

branch = input("Enter your branch name: ").strip()
passing_year = int(input("Enter your passing year: "))
college_name = input("Enter your college name: ").strip()

graduation_cgpa = float(input("Enter your graduation CGPA: "))
inter_percentage = float(input("Enter your inter percentage: "))
ssc_percentage = float(input("Enter your SSC percentage: "))

skills = set(map(str.strip, input(
    "Enter your skills (comma separated): "
).split(",")))

experience = input(
    "Enter your experience (or type 'No Experience'): "
).strip()

projects = input("Enter your project details: ").strip()

preferred_roles = tuple(map(str.strip, input(
    "Enter your preferred roles (comma separated): "
).split(",")))

preferred_locations = list(map(str.strip, input(
    "Enter your preferred locations (comma separated): "
).split(",")))

print("\n", "="*20, "YOUR DETAILS", "="*20)

print("Name               :", name)
print("Address            :", address)
print("Mobile Number      :", mobile_number)
print("Email ID           :", email_id)
print("Qualification      :", qualification)
print("Branch             :", branch)
print("Passing Year       :", passing_year)
print("College Name       :", college_name)
print("Graduation CGPA    :", graduation_cgpa)
print("Inter Percentage   :", inter_percentage)
print("SSC Percentage     :", ssc_percentage)
print("Skills             :", ", ".join(skills))
print("Experience         :", experience)
print("Projects           :", projects)
print("Preferred Roles    :", ", ".join(preferred_roles))
print("Preferred Location :", ", ".join(preferred_locations))


