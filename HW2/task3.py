from cipher import encrypt, decrypt

expected_table = {
    "asamant": "Temp123",
    "aissa": "TheKing%^&",
    "bjha": "$72messenger",
    "skharel": "Life15$",
    "Ally!": "God$12"
}

N = 3
D = 1

# Read and parse database
database = {}
with open("database.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            userid_enc, passwd_enc = line.split()
            database[decrypt(userid_enc, N, D)] = decrypt(passwd_enc, N, D)

# Q1: Exact matches in database
q1 = [(uid, pwd) for uid, pwd in expected_table.items() if database.get(uid) == pwd]

# Q2: Userids in database with mismatched passwords
q2 = [(uid, database[uid]) for uid, pwd in expected_table.items() if uid in database and database[uid] != pwd]

# Q3: Invalid userids (containing characters outside ASCII 34-126)
q3 = [uid for uid in expected_table if any(ord(c) < 34 or ord(c) > 126 for c in uid)]

# Print results
print("Q1. userid/password combinations present in database:")
for uid, pwd in q1:
    print(f"  {uid} | {pwd}")
if not q1:
    print("  None")

print("\nQ2. userids in database with mismatched password:")
for uid, db_pwd in q2:
    print(f"  {uid} | Table: {expected_table[uid]}, Database: {db_pwd}")
if not q2:
    print("  None")

print("\nQ3. userids that don't meet cipher validation requirements:")
for uid in q3:
    print(f"  {uid}")
if not q3:
    print("  None")

# Q1. Which userid/password combinations from the table are present in the database?
# Answer: asamant | Temp123, skharel | Life15$

# Q2. Which userids are present in the database, but the password in the table does not match the stored password?
# Answer: aissa (database has Light%^&, table has TheKing%^&), bjha (database has $72Hello, table has $72messenger)

# Q3. Which userids do not meet the requirements of a userid? (containing invalid characters like space or !)
# Answer: Ally!
