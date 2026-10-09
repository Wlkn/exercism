import csv

users_csv = []

with open(r'python-iam\day2\users.csv', mode="r", newline="", encoding="utf-8") as users:
    reader = csv.DictReader(users)
    for row in reader:
        users_csv.append(dict(row))

# How many users each department has x
# Emails used by more than one person (ignore uppercase vs lowercase)
# Users with no manager
# Interns in the admins group, which is a real security finding
#find how many users each department has

def how_many_users_in_each_dep(users_csv):
    counts = {}
    # for row in users_csv:
    #     print(row["department"])
    for row in users_csv:
        counts[row["department"]] = counts.get(row["department"], 0) + 1
    return counts
# how_many_users_in_each_dep(users_csv)

def duplicate_emails(users_csv):
    names_by_email = {}
    for row in users_csv:
        email_row = row["email"].lower()
        name_row = row["name"]

        if email_row not in names_by_email:
            names_by_email[email_row] = []

        names_by_email[email_row].append(name_row)

    duplicates = {email: names for email, names in names_by_email.items() if len(names) >= 2}
    return duplicates

print(duplicate_emails(users_csv))
