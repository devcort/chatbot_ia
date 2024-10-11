import os
import openai

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "NULL"

def chat_whit_llama (prompt):
    response = openai.ChatCompletion.create(
        model= "gpt-4-0613",
        messages = [{"role":"user","content":prompt}],
        temperature = 1
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        human_input = input("Human: ")
        
        if human_input.lower() in ["quit","exit","bye"]:
            break
        
        response = chat_whit_llama(human_input)
        
        print("Chatbot: ", response)