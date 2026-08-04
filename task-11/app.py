import os
import gradio as gr

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap');

:root {
  --bg: #f3f5f8;
  --surface: #ffffff;
  --ink: #111827;
  --muted: #6b7280;
  --line: #e5e7eb;
  --line-strong: #d1d5db;
  --accent: #7c9cff;
  --accent-ink: #1e293b;
  --bot: #f8fafc;
  --user: #eef2ff;
  --shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
  --radius: 16px;
  --app-max: 820px;
}

* { box-sizing: border-box; }

html, body, .gradio-container, .main, .wrap, .app, .contain {
  background: var(--bg) !important;
  font-family: "IBM Plex Sans", sans-serif !important;
  color: var(--ink) !important;
  color-scheme: light !important;
}

.gradio-container {
  max-width: var(--app-max) !important;
  margin: 0 auto !important;
  padding: 0 !important;
  min-height: 100vh;
}

footer, .footer { display: none !important; }

/* Kill dark-mode navy leftovers */
.dark, .dark .block, .dark .bot, .dark .user {
  color-scheme: light !important;
}

/* ===== App shell ===== */
#app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg);
}

/* ===== Header ===== */
#topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 18px;
  background: var(--surface);
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 20;
}

#brand {
  display: flex;
  align-items: center;
  gap: 10px;
}

#brand .logo {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: linear-gradient(145deg, #9db4ff, #7c9cff);
  display: grid;
  place-items: center;
  color: #0f172a;
  font-weight: 700;
  font-size: 0.95rem;
  box-shadow: 0 4px 12px rgba(124, 156, 255, 0.35);
}

#brand .title {
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink);
}

#clear-btn {
  background: transparent !important;
  border: 1px solid var(--line) !important;
  color: var(--muted) !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.08em !important;
  border-radius: 10px !important;
  min-height: 36px !important;
  padding: 0 14px !important;
  box-shadow: none !important;
}

#clear-btn:hover {
  color: var(--ink) !important;
  border-color: var(--line-strong) !important;
  background: #f9fafb !important;
}

/* ===== Body ===== */
#main-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 16px 18px 110px;
}

/* Upload card */
#doc-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 14px;
  box-shadow: var(--shadow);
}

#doc-card .heading {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--muted);
  margin: 0 0 10px;
  letter-spacing: 0.02em;
}

.file-preview,
.upload-container,
[data-testid="file"],
#doc-card .block {
  background: #f8fafc !important;
  border: 1.5px dashed #c7d2fe !important;
  border-radius: 14px !important;
  color: var(--ink) !important;
  min-height: 96px !important;
}

#doc-card .or-label,
#doc-card span,
#doc-card label {
  color: var(--muted) !important;
  font-weight: 500 !important;
}

#analyze-row {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-top: 10px;
}

#statusbox textarea {
  background: #f8fafc !important;
  border: 1px solid var(--line) !important;
  border-radius: 12px !important;
  color: var(--ink) !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
  min-height: 44px !important;
}

#statusbox label { display: none !important; }

#analyze-btn {
  background: var(--accent) !important;
  color: var(--accent-ink) !important;
  border: none !important;
  border-radius: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 0.04em !important;
  min-height: 44px !important;
  min-width: 110px !important;
  box-shadow: 0 6px 16px rgba(124, 156, 255, 0.35) !important;
}

#analyze-btn:hover {
  filter: brightness(0.97);
  transform: translateY(-1px);
}

/* Chat */
#chatbot {
  background: transparent !important;
  border: none !important;
  flex: 1;
  min-height: 360px !important;
}

#chatbot .bot,
#chatbot .assistant,
#chatbot [data-testid="bot"] {
  background: var(--surface) !important;
  color: var(--ink) !important;
  border: 1px solid var(--line) !important;
  border-radius: 16px 16px 16px 6px !important;
  box-shadow: var(--shadow) !important;
  font-size: 0.95rem !important;
  line-height: 1.5 !important;
}

#chatbot .user,
#chatbot [data-testid="user"] {
  background: var(--user) !important;
  color: var(--ink) !important;
  border: 1px solid #dde3ff !important;
  border-radius: 16px 16px 6px 16px !important;
  font-size: 0.95rem !important;
}

#chatbot .bot code,
#chatbot .assistant code,
#chatbot code {
  font-family: "IBM Plex Mono", monospace !important;
  font-size: 0.75rem !important;
  background: #eef2ff !important;
  color: #3730a3 !important;
  border: 1px solid #e0e7ff !important;
  border-radius: 8px !important;
  padding: 4px 8px !important;
  display: inline-block;
  margin: 4px 4px 0 0;
}

/* Sticky composer */
#composer-bar {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  width: min(100%, var(--app-max));
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid var(--line);
  padding: 12px 14px calc(12px + env(safe-area-inset-bottom));
  z-index: 30;
}

#composer-row {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 6px;
  box-shadow: var(--shadow);
}

#plus-btn {
  width: 40px !important;
  min-width: 40px !important;
  height: 40px !important;
  min-height: 40px !important;
  border-radius: 50% !important;
  border: 1px solid var(--line) !important;
  background: #f8fafc !important;
  color: var(--muted) !important;
  font-size: 1.2rem !important;
  font-weight: 600 !important;
  box-shadow: none !important;
  padding: 0 !important;
}

#msgbox textarea {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  min-height: 42px !important;
  font-size: 16px !important;
  padding: 10px 8px !important;
  color: var(--ink) !important;
}

#msgbox textarea:focus {
  outline: none !important;
  box-shadow: none !important;
}

#msgbox label { display: none !important; }

#send-btn {
  width: 44px !important;
  min-width: 44px !important;
  height: 44px !important;
  min-height: 44px !important;
  border-radius: 12px !important;
  background: var(--accent) !important;
  color: var(--accent-ink) !important;
  border: none !important;
  font-size: 1.05rem !important;
  font-weight: 700 !important;
  box-shadow: 0 6px 14px rgba(124, 156, 255, 0.35) !important;
  padding: 0 !important;
}

#send-btn:hover {
  filter: brightness(0.97);
}

button.primary {
  background: var(--accent) !important;
  color: var(--accent-ink) !important;
}

/* Desktop polish */
@media (min-width: 900px) {
  :root { --app-max: 880px; }

  #main-col {
    padding: 20px 24px 120px;
    gap: 16px;
  }

  #doc-card {
    padding: 18px;
  }

  #chatbot {
    min-height: 480px !important;
  }

  #topbar {
    padding: 16px 24px;
    border-radius: 0 0 0 0;
  }
}

/* Mobile */
@media (max-width: 640px) {
  #topbar { padding: 12px 14px; }
  #main-col { padding: 12px 12px 118px; gap: 12px; }
  #doc-card { padding: 12px; border-radius: 14px; }
  #analyze-row { flex-direction: column; align-items: stretch; }
  #analyze-btn { width: 100% !important; }
  #brand .title { font-size: 0.98rem; }
  #chatbot { min-height: 42vh !important; }
}
"""

TOPBAR_LEFT = """
<div id="brand">
  <div class="logo">F</div>
  <div class="title">Folio Clarity</div>
</div>
"""


def upload_pdf(file):
    from chatbot import process_pdf

    if file is None:
        return "No PDF selected"

    try:
        path = file if isinstance(file, str) else getattr(file, "name", None)
        if not path:
            return "Could not read file"
        info = process_pdf(path)
        name = os.path.basename(path)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        return f"{name}  ·  {size_mb:.1f} MB  ·  {info}"
    except Exception as exc:
        return f"Analyze failed · {exc}"


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


def clear_all():
    from chatbot import reset_session

    reset_session()
    return [], "", "No PDF selected"


theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("IBM Plex Sans"),
    font_mono=gr.themes.GoogleFont("IBM Plex Mono"),
).set(
    body_background_fill="#f3f5f8",
    block_background_fill="#ffffff",
    block_border_color="#e5e7eb",
    body_text_color="#111827",
    button_primary_background_fill="#7c9cff",
    button_primary_text_color="#1e293b",
)


with gr.Blocks(title="Folio Clarity", theme=theme, css=CUSTOM_CSS) as demo:
    with gr.Column(elem_id="app-shell"):
        with gr.Row(elem_id="topbar"):
            gr.HTML(TOPBAR_LEFT)
            clear_btn = gr.Button("CLEAR", elem_id="clear-btn")

        with gr.Column(elem_id="main-col"):
            with gr.Column(elem_id="doc-card"):
                gr.HTML("<p class='heading'>Document</p>")
                pdf = gr.File(
                    label="Drop PDF here or click to browse",
                    file_types=[".pdf"],
                    type="filepath",
                    height=110,
                )
                with gr.Row(elem_id="analyze-row"):
                    status = gr.Textbox(
                        value="No PDF selected",
                        interactive=False,
                        show_label=False,
                        scale=4,
                        elem_id="statusbox",
                    )
                    analyze_btn = gr.Button("ANALYZE", elem_id="analyze-btn", scale=1)

            chatbot = gr.Chatbot(
                show_label=False,
                height=460,
                elem_id="chatbot",
                type="messages",
                bubble_full_width=False,
                placeholder="Analyze a PDF, then ask questions about it…",
            )

        with gr.Column(elem_id="composer-bar"):
            with gr.Row(elem_id="composer-row"):
                plus_btn = gr.Button("+", elem_id="plus-btn", scale=0)
                msg = gr.Textbox(
                    placeholder="Ask about the document...",
                    show_label=False,
                    container=False,
                    scale=6,
                    elem_id="msgbox",
                    autofocus=True,
                )
                send_btn = gr.Button("➤", elem_id="send-btn", scale=0)

    analyze_btn.click(upload_pdf, inputs=pdf, outputs=status)
    # + focuses workflow back to upload by showing status hint
    plus_btn.click(
        lambda: "Use the Document card above to attach a PDF",
        outputs=status,
    )
    send_btn.click(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(chat, inputs=[msg, chatbot], outputs=[chatbot, msg])
    clear_btn.click(clear_all, outputs=[chatbot, msg, status])


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
