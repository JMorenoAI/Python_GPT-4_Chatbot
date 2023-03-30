import openai

openai.api_key = "YOUR OPENAI API KEY HERE"

messages = []
system_msg = input("What type of chatbot would you like to create? ")
messages.append({"role": "system", "content": system_msg})

print("Say hello to your new assistant!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")