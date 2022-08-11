from ai import AI

wesker = AI()

wesker.start.trigger()

wesker.say("Hello")
while True and command not in ["good bye", 'bye', 'quit', 'exit','goodbye', 'the exit']:
    command = ""
    command = wesker.listen()
    if command:
        command = command.lower()
        print(f'command heard: {command}') 
        for skill in skills:
            if command in skill.commands(command):
                skill.handle_command(command, wesker)
  
wesker.say("See you soon, dear.")

# tell the plugins the server is shutting down
wesker.stop.trigger()
