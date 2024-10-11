const express = require('express');
const axios = require('axios');
const cors = require('cors')

const { Configuration, OpenAI } = require("openai");

const openai = new OpenAI({
        apiKey: '',
        baseURL: 'http://localhost:1234/v1',
});

const app = express();
const port = 3000;
app.use(cors());
app.use(express.json());

// Ruta para manejar las solicitudes del chat
app.post('/chat', async (req, res) => {
    const userInput = req.body.userInput;
console.log("server post"+userInput);
    // Conecta con OpenAI GPT-3.5
    const response = await getResponse(userInput);

    res.json( response );
});

// Función para generar respuestas del chat usando OpenAI API

const getResponse = async (userInput) => {
    console.log("getresponse"+userInput);
    const response= await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages:[
            {
            role: 'user',
            content: userInput,
            },
        ],
        temperature: 0,
        max_tokens: 500,
        top_p:1.0,
        frecuency_penalty: 0.0,
        presence_penalty:0.0,
        
    });
    //console.log(response.choices[0].message.content);
    return response.choices[0].message.content
};


// Inicia el servidor
app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});
