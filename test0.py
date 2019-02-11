from sys import argv

if len(argv) <= 1:
    print('You didn\'t identify yourself.')
    user = input('Who are you, stranger? ')
else:
    filename, user = argv

print(f'Hola {user}!')
# print('Hola %s!' % user)

another_user = input('Who is yout best friend? ')
i = 1

while another_user == user and i == 1:
    print(f'Sorry {user}, but you gave your own name.')
    another_user = input('Who is your bestie? ')
    i += 1

if another_user == user:
    print('So you have a best friend with your own name?? Great! ^^')
    print('or maybe you are your own best friend... it\'s cool, I guess...')
else:
    print('So, {} is your bestie! I\'m glad to read that!'.format(another_user))

# print('Hola %s' % another_user + '!')
