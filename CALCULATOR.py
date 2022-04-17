#minha calculadora
import sys
diss = input('Are you stupid when it comes to numbers?')
if diss == 'yes':
    print('What a shame. Depending on a machine, innit?') 
else: print('So get the FUCK outta here'), sys.exit()
# add
def add(x, y):
    return x + y
# subtract
def subtract(x, y):
    return x - y
# multiply
def multiply(x, y):
    return x * y
# divide
def divide(x, y):
    return x / y
print("Imma help you this time. Say what you want to do.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operacao = input('Im a little stupid bitch that wants to:')
if operacao == '1':
    print('So you need a machines help to ADD some numbers? Wow, humanity has sure come far.')
elif operacao == '2':
    print('Sure, sure... Have you ever considered that it costs you money to ask me to do this for you?')
elif operacao == '3':
    print('Im not Jesus but yeah, I can multiply stuff. Fun fact: I cant be crucified.')
elif operacao == '4':
    print('Damn. Hope you are not a communist.')
else: print('I could see you are dumb, but I was not expecting THAT...'), sys.exit()
    
print("Anyway.")
while True:
    if operacao in ('1', '2', '3', '4'):
        x = int(input('Type the first number to this equation:'))
        y = int(input('Type the second number to this equation:'))
        if operacao == '1':
            print('... it was even more stupid than I had anticipated. 86 BILLION neurons, and still you did not figure that the answer is', add(x, y), "?")
        elif operacao == '2':
            print(subtract(x, y), 'neurons were subtracted from your brain when you decided to ask me for the answer. Yeah,', subtract(x, y),'is the answer.')
        elif operacao == '3':
            print('Taking the', x, 'loaves and the', y, 'fish and looking up to heaven, Jesus said:')
            print('Tell this whore the answer is', multiply(x, y))
        elif operacao == '4':
            print('Did you really just consume electricity... for this? The answer is', divide(x, y), ', Einstein.')
