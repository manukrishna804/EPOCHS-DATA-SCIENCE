import os
import gradio as gr

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
  --ink: #10233f;
  --muted: #5b6b7c;
  --line: rgba(16, 35, 63, 0.10);
  --accent: #0f766e;
  --accent-soft: #d8f3ef;
  --surface: rgba(255, 255, 255, 0.86);
  --shadow: 0 18px 50px rgba(16, 35, 63, 0.08);
}

.gradio-container {
  max-width: 1080px !important;
  margin: 0 auto !important;
  font-family: "Plus Jakarta Sans", sans-serif !important;
  color: var(--ink) !important;
}

/* Soft white atmosphere — cool mist, not flat white */
body, .gradio-container, .main, .wrap {
  background:
    radial-gradient(1200px 600px at 12% -10%, #e8f4ff 0%, transparent 55%),
    radial-gradient(900px 500px at 100% 0%, #e7f7f3 0%, transparent 50%),
    linear-gradient(180deg, #f7fafc 0%, #ffffff 45%, #f4f7fa 100%) !important;
}

footer, .footer, .svelte-1ipelgc { display: none !important; }

#brand {
  text-align: center;
  padding: 28px 12px 8px;
  animation: rise 0.7s ease both;
}

#brand h1 {
  font-family: "Fraunces", serif !important;
  font-size: clamp(2.4rem, 5vw, 3.4rem) !important;
  font-weight: 700 !important;
  letter-spacing: -0.03em;
  color: var(--ink) !important;
  margin: 0 0 8px !important;
}

#brand p {
  font-size: 1.05rem;
  color: var(--muted);
  margin: 0 auto;
  max-width: 34rem;
  line-height: 1.55;
}

#panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 24px;
  padding: 22px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(10px);
  animation: rise 0.85s ease both;
}

#statusbox textarea {
  background: #f3faf8 !important;
  border: 1px solid #cfe8e3 !important;
  color: var(--accent) !important;
  font-weight: 600 !important;
  border-radius: 14px !important;
}

button.primary, .primary {
  background: var(--ink) !important;
  border: none !important;
  color: white !important;
  border-radius: 14px !important;
  font-weight: 600 !important;
  transition: transform 0.18s ease, background 0.18s ease !important;
}

button.primary:hover, .primary:hover {
  background: var(--accent) !important;
  transform: translateY(-1px);
}

button.secondary, .secondary {
  background: white !important;
  border: 1px solid var(--line) !important;
  color: var(--ink) !important;
  border-radius: 14px !important;
}

#chatbot {
  border: 1px solid var(--line) !important;
  border-radius: 18px !important;
  background: #ffffff !important;
  min-height: 420px;
}

#composer textarea {
  border-radius: 16px !important;
  border: 1px solid var(--line) !important;
  background: #fff !important;
  min-height: 52px !important;
}

.file-preview, .upload-container, [data-testid="file"] {
  border-radius: 16px !important;
  border: 1px dashed rgba(15, 118, 110, 0.35) !important;
  background: linear-gradient(180deg, #ffffff, #f7fffd) !important;
}

@keyframes rise {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
  #panel { padding: 14px; border-radius: 18px; }
  #brand { padding-top: 16px; }
}
"""


def upload_pdf(file):
    from chatbot import process_pdf

    if file is None:
        return "Please upload a PDF first."

    try:
        path = file if isinstance(file, str) else getattr(file, "name", None)
        if not path:
            return "Could not read the uploaded file."
        message = process_pdf(path)
        name = os.path.basename(path)
        return f"{name} ready — {message}"
    except Exception as exc:
        return f"Could not process PDF: {exc}"


def chat(message, history):
    from chatbot import ask_question

    history = history or []
    message = (message or "").strip()
    if not message:
        return history, ""

    try:
        answer = ask_question(message)
    except Exception as exc:
        answer = f"Something went wrong: {exc}"

    history = history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": answer},
    ]
    return history, ""


def clear_chat():
    from chatbot import clear_memory

    clear_memory()
    return [], ""


theme = gr.themes.Soft(
    primary_hue="teal",
    secondary_hue="slate",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("Plus Jakarta Sans"),
).set(
    body_background_fill="#ffffff",
    block_background_fill="#ffffff",
    border_color_primary="rgba(16,35,63,0.10)",
    button_primary_background_fill="#10233f",
    button_primary_background_fill_hover="#0f766e",
    button_primary_text_color="#ffffff",
)


with gr.Blocks(title="Folio — PDF Chat", theme=theme, css=CUSTOM_CSS) as demo:
    with gr.Column(elem_id="brand"):
        gr.Markdown("# Folio")
        gr.Markdown(
            "Ask clear questions about any PDF. Upload a document, process it, then chat."
        )

    with gr.Column(elem_id="panel"):
        with gr.Row():
            pdf = gr.File(
                label="Upload PDF",
                file_types=[".pdf"],
                type="filepath",
                scale=4,
            )
            process_btn = gr.Button("Process PDF", variant="primary", scale=1)

        status = gr.Textbox(
            label="Status",
            value="Waiting for a PDF…",
            interactive=False,
            elem_id="statusbox",
        )

        chatbot = gr.Chatbot(
            label="Conversation",
            height=460,
            elem_id="chatbot",
            show_label=True,
            type="messages",
        )

        with gr.Row():
            msg = gr.Textbox(
                placeholder="Ask anything about the PDF…",
                show_label=False,
                scale=8,
                elem_id="composer",
                container=False,
            )
            send_btn = gr.Button("Send", variant="primary", scale=1)

        clear_btn = gr.Button("Clear chat", variant="secondary")

    process_btn.click(upload_pdf, inputs=pdf, outputs=status)
    send_btn.click(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear_btn.click(clear_chat, outputs=[chatbot, msg])


# Hugging Face Spaces imports this module and finds `demo`
demo.queue(default_concurrency_limit=1)

if __name__ == "__main__":
    # Spaces / Render / Railway set PORT; bind all interfaces there
    hosted = any(
        key in os.environ
        for key in ("PORT", "RENDER", "SPACE_ID", "SPACE_HOST")
    )
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0" if hosted else "127.0.0.1",
        server_port=port,
        share=False,
        show_error=True,
    )
