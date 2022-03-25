import emoji
from time import sleep
for cont in range(10, 0, -1):
    print(cont)
    sleep(1)
print('ACABOU!')
print('BUM! BUM! POOW!')
print(emoji.emojize("FOGOS ESTOURADOS! \033[31m:fireworks: \033[31m:fireworks: \033[31m:fireworks: ", use_aliases=True))
