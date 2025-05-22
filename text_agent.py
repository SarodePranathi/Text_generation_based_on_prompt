import requests

# Replace this with your actual API key
API_KEY = 'enter the API key after generating it from aimlapi'
API_URL = 'https://api.aimlapi.com/v1/chat/completions'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'user', 'content': user_input}
        ],
        'temperature': 0.7,
        'max_tokens': 500
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200 or response.status_code == 201:
        reply = response.json()['choices'][0]['message']['content']
        print("\nGenerated Text:\n", reply)
    else:
        print(f"Error: {response.status_code} - {response.text}")
