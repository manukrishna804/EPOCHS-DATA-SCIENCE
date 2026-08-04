import gradio as gr
from chatbot import process_pdf, ask_question, clear_memory

css = """
body{
    background:#f7f7f8;
}

.gradio-container{
    max-width:1300px !important;
    margin:auto;
}

.block{
    border-radius:18px !important;
}

footer{
    display:none !important;
}

h1{
    text-align:center;
}

#header{
    text-align:center;
    margin-bottom:20px;
}

#sidebar{
    background:white;
    border-radius:18px;
    padding:20px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}

#chatcard{
    background:white;
    border-radius:18px;
    padding:15px;
    box-shadow:0 2px 8px rgba(0,0,0,.08);
}

textarea{
    border-radius:14px !important;
}

button{
    border-radius:12px !important;
}

.message{
    border-radius:16px !important;
}
"""


def upload_pdf(file):

    if file is None:
        return "❌ Please upload a PDF."

    process_pdf(file.name)

    filename = file.name.split("/")[-1].split("\\")[-1]

    return f"✅ {filename} processed successfully."


def chat(message, history):

    answer = ask_question(message)

    history.append(
        {
            "role":"user",
            "content":message
        }
    )

    history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    return history,""


def clear_chat():

    clear_memory()

    return [],""


with gr.Blocks(
    title="PDF RAG Chatbot",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown("# 📄 PDF RAG Chat Assistant")

    gr.Markdown(
        "Upload a PDF and ask questions about its contents."
    )

    with gr.Row():

        pdf = gr.File(
            label="Upload PDF",
            file_types=[".pdf"],
            scale=4
        )

        process_btn = gr.Button(
            "Process PDF",
            variant="primary",
            scale=1
        )

    status = gr.Textbox(
        label="Status",
        interactive=False
    )

    chatbot = gr.Chatbot(
        label="Conversation",
        height=550
    )

    with gr.Row():

        msg = gr.Textbox(
            placeholder="Ask anything about the PDF...",
            show_label=False,
            scale=8
        )

        send_btn = gr.Button(
            "Send",
            variant="primary",
            scale=1
        )

    clear_btn = gr.Button("Clear Chat")

    process_btn.click(
        upload_pdf,
        inputs=pdf,
        outputs=status
    )

    send_btn.click(
        chat,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    msg.submit(
        chat,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    clear_btn.click(
        clear_chat,
        outputs=[chatbot, msg]
    )

demo.launch()