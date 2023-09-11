from dict import chat_dict, symptom_to_disease, lang, keyword_urls
from flask import Flask, render_template, request, jsonify
import requests
import webbrowser
from translate import Translator
from bs4 import BeautifulSoup
from datetime import datetime
import time

app = Flask(__name__)

last_user_activity = time.time()
reminder_sent1 = False
reminder_sent2 = False
REMINDER_INTERVAL = 15
NO_RESPONSE_INTERVAL = 30
conversation_history = []

def open_webpage(url):
    webbrowser.open(url)

def filter_text(text):
    result = "".join(char for char in text if char.isalnum() or char.isspace())
    return result

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    search_result = soup.find("div", class_="BNeawe").text
    return search_result

def get_possible_disease(symptoms):
    possible_diseases = set()
    for symptom in symptoms:
        if symptom in symptom_to_disease:
            possible_diseases.update(symptom_to_disease[symptom])
    return list(possible_diseases)

def translate_text(text, target_language):
    translator = Translator(from_lang='en', to_lang=lang.get(target_language.lower()))
    sentences = text.split('. ')
    translated_sentences = []
    for sentence in sentences:
        translation = translator.translate(sentence)
        translated_sentences.append(translation)
    translated_text = '. '.join(translated_sentences)
    return translated_text
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global last_user_activity, reminder_sent1, reminder_sent2

    user_message = request.form.get('user_message')
    last_user_activity = time.time()
    user_input = request.form['user_message'].lower()
    user_input = filter_text(user_input)
    response = ""
    reminder_sent1 = False
    reminder_sent2 = False
    user_symptoms = []  
    try:
        if user_input == 'bye':
            response = "Durgss: Goodbye!"
        elif user_input.startswith('translate'):
            translation_input = user_input.replace('translate', '').strip()
            translation_parts = translation_input.split('to')
            if len(translation_parts) == 2:
                text_to_translate = translation_parts[0].strip()
                target_language = translation_parts[1].strip()
                translated_text = translate_text(text_to_translate, target_language)
                response = f"Durgss: Translated text: {translated_text}"
            else:
                response = "Durgss: Invalid translation request. Please provide a text to translate and a target language."
        elif user_input in chat_dict:
            response = "Durgss: " + chat_dict[user_input]
        else:
            for symptom_keyword in symptom_to_disease:
                if symptom_keyword in user_input:
                    user_symptoms.append(symptom_keyword)

            if not user_symptoms:
                for keyword, url in keyword_urls.items():
                    if keyword in user_input:
                        open_webpage(url)
                        response += "\nDurgss: Opening... "
                        break

            if user_symptoms:
                possible_diseases = get_possible_disease(user_symptoms)

                if possible_diseases:
                    response += "\nDurgss: Possible diseases based on your symptoms:\n"
                    for disease in possible_diseases:
                        response += "- " + disease + "\n"
                else:
                    response += "\nDurgss: No specific disease could be identified based on the symptoms provided."
            
            if not response:
                search_result = search_google(user_input)
                response = "Durgss: " + search_result
                reminder_sent = False
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        response = "Durgss: Oops! Something went wrong. Please try again later."

    return jsonify({'message': response})

@app.route('/check_activity')
def check_activity():
    global last_user_activity, reminder_sent1, reminder_sent2, REMINDER_INTERVAL, NO_RESPONSE_INTERVAL

    current_time = time.time()
    time_since_activity = current_time - last_user_activity
    
    reminder_condition = time_since_activity >= REMINDER_INTERVAL and not reminder_sent1
    no_response_condition = time_since_activity >= NO_RESPONSE_INTERVAL and not reminder_sent2

    if reminder_condition:
        reminder_message = "Durgss: Hey, are you there?"
        response = {'message': reminder_message}
        reminder_sent1 = True
    elif no_response_condition:
        reminder_message = "Durgss: Hello, can you hear me? Please type something. I'm waiting for your response."
        response = {'message': reminder_message}
        reminder_sent2 = True
      
    else:
        # If there has been recent activity, send an empty response
        response = {'message': ''}

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
