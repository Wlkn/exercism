import sys

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt + "\n")
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


if ask_ok("Do you want to delete it? "):
    print("Deleting...")
else:
    print("Keeping it.")
