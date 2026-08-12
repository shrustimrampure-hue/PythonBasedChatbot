import google.generativeai as genai
# Put your Gemini API key here
genai.configure(api_key="API_KEY")
model = genai.GenerativeModel("gemini-3.6-flash")
print("Chatbot is ready! Type 'exit' to stop\n")
while True:
    user_input = input("YOU: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = model.generate_content(user_input)
    print("Chatbot: ",response.text)
    