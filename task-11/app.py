import os
import gradio as gr

# Tidio-style live-chat widget — white body, blue header, bubble chat

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

:root {
  --blue: #2f7bf6;
  --blue-2: #1a6aef;
  --blue-soft: #e8f1ff;
  --ink: #1f2937;
  --muted: #8b95a5;
  --line: #e8edf3;
  --widget-w: 400px;
}

html, body, .gradio-container, .main, .wrap, .app, .contain {
  background: #e9eef5 !important;
  font-family: "Nunito", sans-serif !important;
  color: var(--ink) !important;
  color-scheme: light !important;
}

/* Kill Gradio auto-dark that paints navy bubbles */
.dark,
.dark body,
.dark .gradio-container,
.dark .block,
.dark .bubble-wrap,
.dark .message,
.dark .bot,
.dark .user {
  background-color: transparent !important;
  color-scheme: light !important;
}

.gradio-container {
  max-width: var(--widget-w) !important;
  margin: 24px auto !important;
  padding: 0 !important;
}

footer, .footer { display: none !important; }

/* ===== Widget shell ===== */
#widget {
  background: #ffffff;
  border-radius: 22px;
  overflow: hidden;
  box-shadow:
    0 18px 50px rgba(30, 60, 120, 0.18),
    0 2px 0 rgba(255,255,255,0.7) inset;
  border: 1px solid rgba(255,255,255,0.6);
  animation: popIn 0.45s cubic-bezier(.22,1,.36,1) both;
}

/* ===== Blue wavy header ===== */
#chat-header {
  position: relative;
  background: linear-gradient(135deg, #4c9bff 0%, #2f7bf6 45%, #1f63e0 100%);
  color: #fff;
  padding: 18px 18px 34px;
  overflow: hidden;
}

#chat-header::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: 28px;
  background:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 28' preserveAspectRatio='none'%3E%3Cpath d='M0 18 C60 28 100 4 160 14 C230 26 280 4 340 16 C370 22 390 20 400 18 L400 28 L0 28 Z' fill='%23ffffff'/%3E%3C/svg%3E")
    center bottom / 100% 28px no-repeat;
}

#chat-header .row {
  display: flex;
  align-items: center;
  gap: 12px;
  position: relative;
  z-index: 1;
}

#chat-header .avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(145deg, #ffe566, #ffc93c);
  border: 3px solid rgba(255,255,255,0.55);
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.25rem;
  color: #1f2937;
  flex-shrink: 0;
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

#chat-header .meta {
  flex: 1;
  min-width: 0;
}

#chat-header .meta .small {
  font-size: 0.78rem;
  opacity: 0.92;
  font-weight: 600;
}

#chat-header .meta .name {
  font-size: 1.22rem;
  font-weight: 800;
  line-height: 1.15;
  margin-top: 1px;
}

#chat-header .meta .online {
  margin-top: 4px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  opacity: 0.9;
}

#chat-header .actions {
  display: flex;
  gap: 10px;
  opacity: 0.95;
  font-size: 1.15rem;
  font-weight: 700;
}

/* ===== Upload strip ===== */
#upload-strip {
  padding: 4px 14px 10px;
  background: #fff;
  border-bottom: 1px solid var(--line);
}

#upload-strip .label-wrap,
#upload-strip label {
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  color: var(--muted) !important;
}

#upload-row {
  display: flex;
  gap: 8px;
  align-items: stretch;
}

.file-preview, .upload-container, [data-testid="file"],
#upload-strip .block {
  background: #f7faff !important;
  border: 1.5px dashed #b7d2ff !important;
  border-radius: 14px !important;
  color: var(--ink) !important;
  min-height: 0 !important;
}

#upload-strip button,
#index-btn {
  background: var(--blue) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 14px !important;
  font-weight: 800 !important;
  min-height: 44px !important;
  box-shadow: 0 6px 14px rgba(47, 123, 246, 0.28) !important;
}

#statusbox textarea {
  background: #eef6ff !important;
  color: var(--blue-2) !important;
  border: none !important;
  border-radius: 12px !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  text-align: center !important;
  min-height: 34px !important;
  padding: 6px 10px !important;
}

#statusbox label { display: none !important; }

/* ===== Chat body ===== */
#chatbot {
  background: #ffffff !important;
  border: none !important;
  border-radius: 0 !important;
  min-height: 380px !important;
}

#chatbot .wrapper,
#chatbot .bubble-gap,
#chatbot [class*="message-row"] {
  background: transparent !important;
}

/* Force LIGHT bubbles — kill Gradio dark navy */
#chatbot .bot,
#chatbot .assistant,
#chatbot [data-testid="bot"],
#chatbot .message.bot,
#chatbot .bubble.bot,
#chatbot .message-content.bot {
  background: #ffffff !important;
  color: var(--ink) !important;
  border: 1px solid #eef2f7 !important;
  border-radius: 18px !important;
  box-shadow: 0 6px 18px rgba(30, 50, 90, 0.08) !important;
  font-size: 0.92rem !important;
  line-height: 1.45 !important;
}

#chatbot .user,
#chatbot [data-testid="user"],
#chatbot .message.user,
#chatbot .bubble.user,
#chatbot .message-content.user {
  background: linear-gradient(135deg, #4c9bff, #2f7bf6) !important;
  color: #ffffff !important;
  border: none !important;
  border-radius: 18px !important;
  box-shadow: 0 8px 18px rgba(47, 123, 246, 0.28) !important;
  font-size: 0.92rem !important;
}

/* Extra Gradio 5 overrides */
#chatbot .prose,
#chatbot p,
#chatbot span {
  color: inherit !important;
}

#chatbot .user .prose,
#chatbot .user p,
#chatbot .user span {
  color: #ffffff !important;
}

/* ===== Composer ===== */
#composer {
  background: #fff;
  border-top: 1px solid var(--line);
  padding: 10px 12px 12px;
}

#composer-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

#msgbox textarea {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  font-size: 15px !important;
  min-height: 44px !important;
  padding: 10px 6px !important;
  color: var(--ink) !important;
  font-family: "Nunito", sans-serif !important;
}

#msgbox textarea:focus {
  outline: none !important;
  box-shadow: none !important;
}

#msgbox label { display: none !important; }

#send-btn {
  width: 48px !important;
  min-width: 48px !important;
  max-width: 48px !important;
  height: 48px !important;
  min-height: 48px !important;
  border-radius: 50% !important;
  padding: 0 !important;
  background: linear-gradient(145deg, #4c9bff, #1f63e0) !important;
  color: #fff !important;
  border: none !important;
  font-size: 1.15rem !important;
  box-shadow: 0 8px 18px rgba(47, 123, 246, 0.35) !important;
  flex-shrink: 0;
}

#send-btn:hover {
  filter: brightness(1.06);
  transform: translateY(-1px);
}

#clear-btn {
  background: transparent !important;
  color: var(--muted) !important;
  border: none !important;
  font-weight: 700 !important;
  font-size: 0.78rem !important;
  min-width: 48px !important;
  box-shadow: none !important;
}

#powered {
  text-align: center;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #a0aab8;
  padding: 2px 0 10px;
  background: #fff;
}

#powered span {
  color: var(--blue);
}

@keyframes popIn {
  from { opacity: 0; transform: translateY(16px) scale(0.97); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

/* Mobile full-bleed */
@media (max-width: 480px) {
  .gradio-container {
    max-width: 100% !important;
    margin: 0 !important;
  }
  #widget {
    border-radius: 0;
    min-height: 100vh;
    box-shadow: none;
  }
  #chatbot {
    min-height: 52vh !important;
  }
}
"""

HEADER_HTML = """
<div id="chat-header">
  <div class="row">
    <div class="avatar">F</div>
    <div class="meta">
      <div class="small">Chat with</div>
      <div class="name">Folio Assistant</div>
      <div class="online">● We're online</div>
    </div>
    <div class="actions" aria-hidden="true">⋮</div>
  </div>
</div>
"""


def upload_pdf(file):
    from chatbot import process_pdf

    if file is None:
        return "Attach a PDF to start"

    try:
        path = file if isinstance(file, str) else getattr(file, "name", None)
        if not path:
            return "Could not read file"
        process_pdf(path)
        return f"Ready · {os.path.basename(path)}"
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


# Force a bright light theme so Gradio stops painting navy cards
theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="blue",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("Nunito"),
).set(
    body_background_fill="#e9eef5",
    block_background_fill="#ffffff",
    block_border_color="#e8edf3",
    block_label_text_color="#1f2937",
    body_text_color="#1f2937",
    button_primary_background_fill="#2f7bf6",
    button_primary_background_fill_hover="#1a6aef",
    button_primary_text_color="#ffffff",
    chatbot_text_size="md",
)


with gr.Blocks(title="Folio Chat", theme=theme, css=CUSTOM_CSS) as demo:
    with gr.Column(elem_id="widget"):
        gr.HTML(HEADER_HTML)

        with gr.Column(elem_id="upload-strip"):
            with gr.Row(elem_id="upload-row"):
                pdf = gr.File(
                    label="PDF",
                    file_types=[".pdf"],
                    type="filepath",
                    scale=3,
                    height=70,
                )
                index_btn = gr.Button("Index", elem_id="index-btn", scale=1)
            status = gr.Textbox(
                value="Attach a PDF to start",
                interactive=False,
                show_label=False,
                max_lines=1,
                elem_id="statusbox",
            )

        chatbot = gr.Chatbot(
            show_label=False,
            height=420,
            elem_id="chatbot",
            type="messages",
            bubble_full_width=False,
            placeholder="Hi! Index a PDF, then ask me anything about it.",
        )

        with gr.Column(elem_id="composer"):
            with gr.Row(elem_id="composer-row"):
                msg = gr.Textbox(
                    placeholder="Enter your message...",
                    show_label=False,
                    container=False,
                    scale=6,
                    elem_id="msgbox",
                    autofocus=True,
                )
                clear_btn = gr.Button("Clear", elem_id="clear-btn", scale=1)
                send_btn = gr.Button("➤", elem_id="send-btn", scale=1)

        gr.HTML('<div id="powered">POWERED BY <span>FOLIO</span></div>')

    index_btn.click(upload_pdf, inputs=pdf, outputs=status)
    send_btn.click(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear_btn.click(clear_chat, outputs=[chatbot, msg])


demo.queue(default_concurrency_limit=1)

if __name__ == "__main__":
    hosted = any(
        key in os.environ for key in ("PORT", "RENDER", "SPACE_ID", "SPACE_HOST")
    )
    port = int(os.environ.get("PORT", 7860))
    demo.launch(
        server_name="0.0.0.0" if hosted else "127.0.0.1",
        server_port=port,
        share=False,
        show_error=True,
    )
