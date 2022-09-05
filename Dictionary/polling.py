favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'python',
    'phil': 'java',
    'jazeb': 'php',
    'brad': 'javascript'
}
new_persons = ['john', 'peter']

for person in set(favourite_language):
    print(person.title() + ' Thank you for taking the poll!')
