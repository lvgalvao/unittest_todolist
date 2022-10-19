from faker import Faker

faker = Faker('pt_BR')

d = {
    'name': faker.cpf()
}

for _ in range(10):
  print(faker.cpf())