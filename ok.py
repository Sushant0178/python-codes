from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate 10,000 unique random names
unique_names = set()

while len(unique_names) < 10000:
    unique_names.add(fake.name())

# Convert the set to a list
random_names = list(unique_names)

# Print the first few names as a sample
print("Sample of Generated Names:", random_names[:10000000])ojjvosdnvozjdjvnkzjdvbkzxjvj kx
