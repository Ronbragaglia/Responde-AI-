# -*- coding: utf-8 -*-
"""Responde AI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tAFPNsGsTU2l2QhKRalTdmUJb0ZZOK9m
"""

!pip install openai gradio


import openai
import gradio as gr


openai.api_key = ''


def study_assistant(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Você é um assistente de estudos especializado em IA e Data Science. Responda de forma clara e didática: {prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


def feedback_correction(prompt, user_answer):
    correction_prompt = f"Aqui está a pergunta: '{prompt}'. A resposta do estudante foi: '{user_answer}'. Corrija a resposta, apontando o que está certo ou errado, e explique a resposta correta."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=correction_prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()


with gr.Blocks() as interface:
    gr.Markdown("# 🤖 Chatbot de Auxílio em Estudos com IA")
    gr.Markdown("Pergunte sobre IA, Data Science ou peça correções de respostas!")

    with gr.Tab("Perguntas Técnicas"):
        question_input = gr.Textbox(label="Digite sua pergunta sobre IA ou Data Science")
        question_output = gr.Textbox(label="Resposta do Assistente")
        question_button = gr.Button("Obter Resposta")

        question_button.click(study_assistant, inputs=question_input, outputs=question_output)

    with gr.Tab("Correção de Respostas"):
        correction_question = gr.Textbox(label="Digite a pergunta")
        user_answer = gr.Textbox(label="Digite sua resposta para correção")
        correction_output = gr.Textbox(label="Correção e Feedback")

        correction_button = gr.Button("Corrigir Resposta")
        correction_button.click(feedback_correction, inputs=[correction_question, user_answer], outputs=correction_output)


interface.launch()