import os
import gradio as gr

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

:root {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --accent: #2563eb;
  --accent-soft: #eff6ff;
  --bot: #ffffff;
  --user: #2563eb;
  --radius: 18px;
  --shadow: 0 8px 28px rgba(15, 23, 42, 0.06);
}

html, body {
  background: var(--bg) !important;
  color-scheme: light !important;
}

.gradio-container {
  max-width: 960px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 !important;
  font-family: "DM Sans", sans-serif !important;
  color: var(--ink) !important;
  background: var(--bg) !important;
}

.main, .wrap, .app, .contain, .dark {
  background: var(--bg) !important;
  color-scheme: light !important;
}

footer, .footer { display: none !important; }

/* Header */
#topbar {
  display: flex !important;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px 20px;
  background: var(--surface) !important;
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 50;
}

#brand-html {
  display: flex;
  align-items: center;
  gap: 12px;
}

#brand-html .mark {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: linear-gradient(145deg, #3b82f6, #1d4ed8);
  color: white;
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: 1.05rem;
  box-shadow: 0 8px 18px rgba(37, 99, 235, 0.28);
}

#brand-html .copy .name {
  font-size: 1.12rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

#brand-html .copy .sub {
  font-size: 0.78rem;
  color: var(--muted);
  margin-top: 2px;
}

#clear-btn {
  background: #fff !important;
  border: 1px solid var(--line) !important;
  color: var(--muted) !important;
  border-radius: 10px !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.06em !important;
  min-height: 38px !important;
  padding: 0 14px !important;
  width: auto !important;
  box-shadow: none !important;
}

#clear-btn:hover {
  color: var(--ink) !important;
  border-color: #cbd5e1 !important;
}

/* Layout */
#page {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-bottom: 120px;
}

#panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 18px;
  box-shadow: var(--shadow);
}

#panel h3 {
  margin: 0 0 4px;
  font-size: 1rem;
  font-weight: 700;
}

#panel p.help {
  margin: 0 0 14px;
  color: var(--muted);
  font-size: 0.88rem;
  line-height: 1.4;
}

/* File upload — hide Gradio's double labels / overlapping UI */
#pdf-file {
  border: 1.5px dashed #93c5fd !important;
  border-radius: 14px !important;
  background: var(--accent-soft) !important;
  padding: 8px !important;
}

#pdf-file .label-wrap,
#pdf-file label,
#pdf-file .or,
#pdf-file span[data-testid="block-info"],
#pdf-file .wrap > label {
  display: none !important;
}

#pdf-file .upload-container,
#pdf-file [data-testid="file"],
#pdf-file .center,
#pdf-file .icon-wrap,
#pdf-file .source-selection {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  min-height: 88px !important;
  color: var(--ink) !important;
}

#pdf-file button,
#pdf-file .upload-button,
#pdf-file .file-button {
  background: transparent !important;
  color: var(--ink) !important;
  border: none !important;
  box-shadow: none !important;
  font-weight: 600 !important;
}

#actions {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  margin-top: 12px;
  align-items: stretch;
}

#statusbox textarea {
  background: #f8fafc !important;
  border: 1px solid var(--line) !important;
  border-radius: 12px !important;
  color: var(--ink) !important;
  font-size: 0.86rem !important;
  font-weight: 500 !important;
  min-height: 46px !important;
}

#statusbox label { display: none !important; }

#analyze-btn {
  background: var(--accent) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 0.04em !important;
  min-width: 130px !important;
  min-height: 46px !important;
  box-shadow: 0 8px 18px rgba(37, 99, 235, 0.25) !important;
}

#analyze-btn:hover {
  background: #1d4ed8 !important;
}

/* Chat */
#chat-panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 8px;
  box-shadow: var(--shadow);
  min-height: 420px;
}

#chatbot {
  background: #fbfdff !important;
  border: none !important;
  border-radius: 14px !important;
  min-height: 400px !important;
}

#chatbot .bot,
#chatbot .assistant,
#chatbot [data-testid="bot"] {
  background: #ffffff !important;
  color: var(--ink) !important;
  border: 1px solid var(--line) !important;
  border-radius: 16px 16px 16px 4px !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04) !important;
}

#chatbot .user,
#chatbot [data-testid="user"] {
  background: var(--user) !important;
  color: #ffffff !important;
  border: none !important;
  border-radius: 16px 16px 4px 16px !important;
}

#chatbot .user *,
#chatbot .user p,
#chatbot .user span {
  color: #ffffff !important;
}

#chatbot code {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace !important;
  font-size: 0.75rem !important;
  background: #eff6ff !important;
  color: #1d4ed8 !important;
  border-radius: 8px !important;
  padding: 3px 8px !important;
  border: 1px solid #dbeafe !important;
}

/* Composer */
#composer {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  width: min(960px, 100%);
  bottom: 0;
  z-index: 60;
  background: rgba(246, 247, 251, 0.92);
  backdrop-filter: blur(10px);
  border-top: 1px solid var(--line);
  padding: 12px 20px calc(12px + env(safe-area-inset-bottom));
}

#composer-box {
  display: flex;
  gap: 8px;
  align-items: center;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 6px;
  box-shadow: var(--shadow);
}

#msgbox textarea {
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  min-height: 44px !important;
  font-size: 16px !important;
  padding: 10px 12px !important;
}

#msgbox textarea:focus {
  outline: none !important;
  box-shadow: none !important;
}

#msgbox label { display: none !important; }

#send-btn {
  background: var(--accent) !important;
  color: #fff !important;
  border: none !important;
  border-radius: 12px !important;
  min-width: 96px !important;
  min-height: 44px !important;
  font-weight: 700 !important;
  box-shadow: 0 8px 16px rgba(37, 99, 235, 0.22) !important;
}

#send-btn:hover { background: #1d4ed8 !important; }

/* Desktop */
@media (min-width: 900px) {
  .gradio-container { max-width: 1040px !important; }
  #page {
    display: grid;
    grid-template-columns: 340px 1fr;
    align-items: start;
    gap: 18px;
    padding: 24px 24px 130px;
  }
  #panel { margin: 0; }
  #chat-panel { margin: 0; min-height: 560px; }
  #chatbot { min-height: 540px !important; }
  #composer { width: min(1040px, 100%); padding-left: 24px; padding-right: 24px; }
}

/* Mobile */
@media (max-width: 899px) {
  #page { padding: 14px 14px 120px; }
  #topbar { padding: 12px 14px; }
  #actions { grid-template-columns: 1fr; }
  #analyze-btn { width: 100% !important; }
  #composer { padding-left: 14px; padding-right: 14px; }
  #chatbot { min-height: 46vh !important; }
}
"""


def analyze_pdf(file):
    from chatbot import process_pdf

    if file is None:
        return "Select a PDF first", []

    try:
        path = file if isinstance(file, str) else getattr(file, "name", None)
        if not path:
            return "Could not read that file", []
        info = process_pdf(path)
        name = os.path.basename(path)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        status = f"{name} · {size_mb:.1f} MB · {info}"
        greeting = {
            "role": "assistant",
            "content": (
                f"I've analyzed **{name}**. Ask me anything about this document.\n\n"
                "Examples: summarize the main points, explain a section, or find a specific detail."
            ),
        }
        return status, [greeting]
    except Exception as exc:
        return f"Failed: {exc}", []


def chat(message, history):
    from chatbot import ask_question

    history = list(history or [])
    message = (message or "").strip()
    if not message:
        return history, ""

    try:
        answer = ask_question(message)
    except Exception as exc:
        answer = f"Something went wrong: {exc}"

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": answer})
    return history, ""


def clear_all():
    from chatbot import reset_session

    reset_session()
    return None, [], "", "No PDF selected"


theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("DM Sans"),
).set(
    body_background_fill="#f6f7fb",
    block_background_fill="#ffffff",
    block_border_color="#e2e8f0",
    body_text_color="#0f172a",
    button_primary_background_fill="#2563eb",
    button_primary_text_color="#ffffff",
)


with gr.Blocks(title="Folio Clarity", theme=theme, css=CUSTOM_CSS) as demo:
    with gr.Row(elem_id="topbar"):
        gr.HTML(
            """
            <div id="brand-html">
              <div class="mark">F</div>
              <div class="copy">
                <div class="name">Folio Clarity</div>
                <div class="sub">PDF question answering</div>
              </div>
            </div>
            """
        )
        clear_btn = gr.Button("CLEAR", elem_id="clear-btn", scale=0)

    with gr.Column(elem_id="page"):
        with gr.Column(elem_id="panel"):
            gr.HTML(
                "<h3>Document</h3>"
                "<p class='help'>Upload a PDF, then click Analyze to index it for chat.</p>"
            )
            pdf = gr.File(
                file_types=[".pdf"],
                type="filepath",
                label=None,
                show_label=False,
                elem_id="pdf-file",
                height=120,
            )
            with gr.Row(elem_id="actions"):
                status = gr.Textbox(
                    value="No PDF selected",
                    interactive=False,
                    show_label=False,
                    elem_id="statusbox",
                    scale=4,
                )
                analyze_btn = gr.Button("ANALYZE", elem_id="analyze-btn", scale=1)

        with gr.Column(elem_id="chat-panel"):
            chatbot = gr.Chatbot(
                show_label=False,
                height=420,
                elem_id="chatbot",
                type="messages",
                bubble_full_width=False,
                placeholder="Your conversation will appear here after you analyze a PDF.",
            )

    with gr.Column(elem_id="composer"):
        with gr.Row(elem_id="composer-box"):
            msg = gr.Textbox(
                placeholder="Ask about the document...",
                show_label=False,
                container=False,
                scale=6,
                elem_id="msgbox",
                autofocus=True,
            )
            send_btn = gr.Button("Send", elem_id="send-btn", scale=1)

    analyze_btn.click(analyze_pdf, inputs=pdf, outputs=[status, chatbot])
    send_btn.click(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear_btn.click(clear_all, outputs=[pdf, chatbot, msg, status])


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
