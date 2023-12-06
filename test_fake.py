from faker import Faker


fake = Faker('sv_SE')

address = fake.address().strip().split('\n')
postnummer, län= address[1].split() 
print(address[0], postnummer, län)

for _ in range(10):
    print(fake.ssn())


print(fake.first_name())
print(fake.last_name())
print(fake.email())
print(fake.date())