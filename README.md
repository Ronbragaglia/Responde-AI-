🤖 Chatbot de Auxílio em Estudos com IA
Este projeto é um assistente virtual educacional desenvolvido com Python que utiliza a API da OpenAI para ajudar estudantes a revisar conteúdos, corrigir respostas e responder perguntas técnicas sobre Inteligência Artificial (IA), Data Science, ou qualquer outra área de interesse.

A interface foi construída com o Gradio, proporcionando uma experiência interativa, acessível diretamente pelo navegador.

🚀 Funcionalidades
📚 Responder Perguntas Técnicas:

O chatbot responde perguntas sobre IA, Machine Learning, Data Science e outros tópicos relacionados.
Utiliza o modelo GPT da OpenAI para fornecer explicações claras e didáticas.
✍️ Correção de Respostas:

O assistente pode corrigir respostas fornecidas por estudantes.
Ele aponta o que está certo ou errado e fornece uma explicação detalhada da resposta correta.
🌐 Interface Intuitiva com Gradio:

A interface permite alternar entre abas para perguntas técnicas e correções.
Fácil de usar e acessível via link compartilhável.
🛠 Tecnologias Utilizadas
Python – Linguagem principal do projeto.
OpenAI API – Para respostas inteligentes e correções.
Gradio – Criação de uma interface web amigável.
Markdown – Para formatação de textos na interface.

🎯 Como Funciona o Código
Importação das Bibliotecas:

As bibliotecas OpenAI e Gradio são instaladas para processamento de linguagem natural e interface web.
Função study_assistant(prompt):

Esta função recebe uma pergunta técnica do usuário e gera uma resposta utilizando o modelo text-davinci-003 da OpenAI.
Função feedback_correction(prompt, user_answer):

Recebe uma pergunta e a resposta do usuário.
O modelo analisa a resposta e fornece uma correção detalhada.
Interface com Gradio:

Duas abas são criadas:
Perguntas Técnicas: Para estudantes fazerem perguntas.
Correção de Respostas: Para o chatbot corrigir e explicar respostas.
Execução da Interface:

A interface é iniciada com interface.launch(), permitindo o uso direto no navegador.

RESULTADO DO CÓDIGO:

![image](https://github.com/user-attachments/assets/a5fbcbc2-aa3b-461d-9a6f-538b44a8ac85)

