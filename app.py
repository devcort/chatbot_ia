from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configuración de OpenAI para usar el servidor local
openai.api_base = "http://localhost:1234/v1"
openai.api_key = ""

@app.route('/')
def home():
    # Renderiza la página principal
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # Obtén la entrada del usuario y verifica que no esté vacía
    user_input = request.form['text'].strip()
    if not user_input:
        # Si la entrada está vacía, envía un mensaje al usuario
        return jsonify({'response': 'Por favor, introduce un mensaje para enviar.'})

    # Llama al chatbot y obtén la respuesta
    response = chat_with_llama(user_input)
    return jsonify({'response': response})
def chat_with_llama(prompt):
    try:
        # Instrucciones del sistema en español
        system_message = "Responde en español de manera fluida y evita usar puntos al final o dentro de las respuestas."

        # Envía la entrada del usuario al servidor de inferencia local y obtén la respuesta
        response = openai.ChatCompletion.create(
            model="local-model",  # Este campo es ignorado por el servidor local pero se deja para compatibilidad
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7  # Puedes ajustar la temperatura según tus necesidades
        )
        # Retorna el contenido de la respuesta del chatbot
        return response.choices[0].message['content']
    except Exception as e:
        # Si hay un error, envía el mensaje de error al usuario
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)
