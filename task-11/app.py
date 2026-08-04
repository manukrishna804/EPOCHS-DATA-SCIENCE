import os
import gradio as gr

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;700&family=Figtree:wght@400;500;600;700&display=swap');

:root {
  --ink: #111827;
  --muted: #6b7280;
  --line: #e5e7eb;
  --soft: #f8fafc;
  --accent: #0d9488;
  --accent-deep: #0f766e;
  --user-bubble: #111827;
  --bot-bubble: #f3f4f6;
  --shadow: 0 10px 40px rgba(17, 24, 39, 0.06);
}

* { box-sizing: border-box; }

.gradio-container {
  max-width: 760px !important;
  margin: 0 auto !important;
  padding: 12px 12px 28px !important;
  font-family: "Figtree", sans-serif !important;
  color: var(--ink) !important;
}

body, .gradio-container, .main, .wrap, .app {
  background:
    radial-gradient(900px 420px at 50% -8%, #ecfeff 0%, transparent 55%),
    linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
}

footer, .footer, footer.svelte-1psgd4h, .svelte-1ipelgc {
  display: none !important;
}

/* Header */
#shell-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 4px 10px;
  animation: fadeUp 0.55s ease both;
}

#shell-header h1 {
  font-family: "Fraunces", serif !important;
  font-size: clamp(1.7rem, 5vw, 2.2rem) !important;
  font-weight: 700 !important;
  letter-spacing: -0.03em;
  margin: 0 !important;
  color: var(--ink) !important;
  line-height: 1.1 !important;
}

#shell-header p {
  margin: 4px 0 0 !important;
  color: var(--muted) !important;
  font-size: 0.92rem !important;
  line-height: 1.4 !important;
}

#status-pill textarea {
  background: #ecfdf5 !important;
  color: var(--accent-deep) !important;
  border: 1px solid #a7f3d0 !important;
  border-radius: 999px !important;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  text-align: center !important;
  min-height: 0 !important;
  padding: 8px 14px !important;
  resize: none !important;
}

#status-pill label { display: none !important; }

/* Upload drawer */
#upload-drawer {
  background: #ffffff;
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 4px 10px 10px;
  box-shadow: var(--shadow);
  margin-bottom: 12px;
  animation: fadeUp 0.65s ease both;
}

#upload-drawer .label-wrap span {
  font-weight: 600 !important;
  color: var(--ink) !important;
}

.file-preview, .upload-container, [data-testid="file"] {
  border-radius: 14px !important;
  border: 1.5px dashed #99f6e4 !important;
  background: #f0fdfa !important;
}

#process-btn {
  min-height: 44px !important;
  border-radius: 12px !important;
  font-weight: 600 !important;
}

/* Chat shell */
#chat-shell {
  background: #ffffff;
  border: 1px solid var(--line);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: var(--shadow);
  animation: fadeUp 0.75s ease both;
}

#chatbot {
  background:
    linear-gradient(180deg, #ffffff 0%, #fafafa 100%) !important;
  border: none !important;
  border-radius: 0 !important;
}

#chatbot .bubble-wrap,
#chatbot [class*="message"],
#chatbot .message-row {
  animation: bubbleIn 0.28s ease both;
}

#chatbot .bot,
#chatbot .assistant,
#chatbot [data-testid="bot"] {
  background: var(--bot-bubble) !important;
  color: var(--ink) !important;
  border-radius: 18px 18px 18px 6px !important;
  border: 1px solid var(--line) !important;
}

#chatbot .user,
#chatbot [data-testid="user"] {
  background: var(--user-bubble) !important;
  color: #ffffff !important;
  border-radius: 18px 18px 6px 18px !important;
}

/* Composer */
#composer-row {
  display: flex;
  gap: 8px;
  align-items: stretch;
  padding: 10px;
  background: #ffffff;
  border-top: 1px solid var(--line);
}

#composer textarea {
  border-radius: 16px !important;
  border: 1px solid var(--line) !important;
  background: var(--soft) !important;
  min-height: 48px !important;
  font-size: 16px !important; /* prevents iOS zoom */
  padding: 12px 14px !important;
}

#composer textarea:focus {
  border-color: #5eead4 !important;
  box-shadow: 0 0 0 3px rgba(13, 148, 136, 0.15) !important;
}

#send-btn, #clear-btn {
  min-height: 48px !important;
  border-radius: 14px !important;
  font-weight: 600 !important;
  white-space: nowrap;
}

#send-btn {
  background: var(--ink) !important;
  color: #fff !important;
  border: none !important;
  min-width: 84px;
  transition: background 0.18s ease, transform 0.18s ease !important;
}

#send-btn:hover {
  background: var(--accent) !important;
  transform: translateY(-1px);
}

#clear-btn {
  background: #fff !important;
  color: var(--muted) !important;
  border: 1px solid var(--line) !important;
  min-width: 72px;
}

button.primary {
  background: var(--ink) !important;
  color: #fff !important;
  border: none !important;
}

button.primary:hover {
  background: var(--accent) !important;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes bubbleIn {
  from { opacity: 0; transform: translateY(6px) scale(0.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

/* Mobile */
@media (max-width: 640px) {
  .gradio-container {
    max-width: 100% !important;
    padding: 8px 8px 20px !important;
  }

  #shell-header {
    flex-direction: column;
    align-items: flex-start;
    padding: 8px 2px 6px;
  }

  #status-pill {
    width: 100%;
  }

  #chat-shell {
    border-radius: 18px;
  }

  #chatbot {
    min-height: 52vh !important;
  }

  #composer-row {
    flex-wrap: wrap;
    padding: 8px;
  }

  #composer {
    flex: 1 1 100%;
  }

  #send-btn, #clear-btn {
    flex: 1 1 auto;
  }

  #upload-drawer {
    border-radius: 14px;
    margin-bottom: 10px;
  }
}
"""


def upload_pdf(file):
    from chatbot import process_pdf

    if file is None:
        return "Upload a PDF to begin"

    try:
        path = file if isinstance(file, str) else getattr(file, "name", None)
        if not path:
            return "Could not read file"
        process_pdf(path)
        name = os.path.basename(path)
        return f"Ready · {name}"
    except Exception as exc:
        return f"Error · {exc}"


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
    secondary_hue="gray",
    neutral_hue="gray",
    font=gr.themes.GoogleFont("Figtree"),
).set(
    body_background_fill="#ffffff",
    block_background_fill="#ffffff",
    border_color_primary="#e5e7eb",
    button_primary_background_fill="#111827",
    button_primary_background_fill_hover="#0d9488",
    button_primary_text_color="#ffffff",
)


with gr.Blocks(title="Folio Chat", theme=theme, css=CUSTOM_CSS, fill_height=True) as demo:
    with gr.Row(elem_id="shell-header"):
        with gr.Column(scale=3):
            gr.Markdown("# Folio")
            gr.Markdown("Your PDF chatbot — upload once, then ask anything.")
        with gr.Column(scale=2, elem_id="status-pill"):
            status = gr.Textbox(
                value="Waiting for PDF",
                interactive=False,
                show_label=False,
                max_lines=1,
            )

    with gr.Accordion("Attach PDF", open=True, elem_id="upload-drawer"):
        with gr.Row():
            pdf = gr.File(
                label="Drop a PDF here",
                file_types=[".pdf"],
                type="filepath",
                scale=3,
            )
            process_btn = gr.Button(
                "Process",
                variant="primary",
                scale=1,
                elem_id="process-btn",
            )

    with gr.Column(elem_id="chat-shell"):
        chatbot = gr.Chatbot(
            label=None,
            show_label=False,
            height=520,
            elem_id="chatbot",
            type="messages",
            bubble_full_width=False,
            avatar_images=(None, None),
            placeholder="Upload a PDF, tap Process, then start chatting…",
        )

        with gr.Row(elem_id="composer-row"):
            msg = gr.Textbox(
                placeholder="Message Folio…",
                show_label=False,
                scale=6,
                elem_id="composer",
                container=False,
                autofocus=True,
            )
            send_btn = gr.Button("Send", variant="primary", scale=1, elem_id="send-btn")
            clear_btn = gr.Button("Clear", scale=1, elem_id="clear-btn")

    process_btn.click(upload_pdf, inputs=pdf, outputs=status)
    send_btn.click(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear_btn.click(clear_chat, outputs=[chatbot, msg])


demo.queue(default_concurrency_limit=1)

if __name__ == "__main__":
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
