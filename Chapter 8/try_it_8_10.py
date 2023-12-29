def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop()
        print(current)
        sent_messages.append(current)

message_list = ['hi', 'hello', 'hey']
sent_messages = []

send_messages(message_list, sent_messages)

print(message_list)
print(sent_messages)