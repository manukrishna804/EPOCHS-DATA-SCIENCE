import os
import gradio as gr

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Sora:wght@300;400;500;600;700&display=swap');

:root {
  --ink: #0b1220;
  --ink-soft: #243044;
  --muted: #64748b;
  --line: rgba(11, 18, 32, 0.08);
  --paper: #ffffff;
  --mist: #f4f7fb;
  --sea: #148f85;
  --sea-deep: #0b6b64;
  --glow: rgba(20, 143, 133, 0.18);
}

html, body {
  min-height: 100%;
}

.gradio-container {
  max-width: 1100px !important;
  margin: 0 auto !important;
  padding: 0 16px 40px !important;
  font-family: "Sora", sans-serif !important;
  color: var(--ink) !important;
}

/* Living white canvas */
body, .gradio-container, .main, .wrap, .app, .contain {
  background:
    radial-gradient(ellipse 80% 50% at 10% -10%, rgba(20, 143, 133, 0.14), transparent 55%),
    radial-gradient(ellipse 70% 45% at 100% 0%, rgba(56, 120, 255, 0.08), transparent 50%),
    radial-gradient(ellipse 60% 40% at 50% 100%, rgba(20, 143, 133, 0.06), transparent 55%),
    linear-gradient(180deg, #fbfcfe 0%, #f3f6fa 48%, #eef3f7 100%) !important;
  background-attachment: fixed !important;
}

/* Subtle paper grain overlay */
.gradio-container::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  opacity: 0.35;
  background-image:
    url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.45'/%3E%3C/svg%3E");
  mix-blend-mode: soft-light;
}

.gradio-container > * {
  position: relative;
  z-index: 1;
}

footer, .footer, footer.svelte-1psgd4h {
  display: none !important;
}

/* ===== HERO ===== */
#hero {
  padding: 36px 8px 18px;
  text-align: center;
  animation: heroIn 0.8s cubic-bezier(.22,1,.36,1) both;
}

#hero .eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--sea-deep);
  margin-bottom: 14px;
}

#hero .eyebrow::before,
#hero .eyebrow::after {
  content: "";
  width: 18px;
  height: 1px;
  background: var(--sea);
  opacity: 0.55;
}

#hero h1 {
  font-family: "Instrument Serif", serif !important;
  font-size: clamp(3.2rem, 10vw, 5.4rem) !important;
  font-weight: 400 !important;
  letter-spacing: -0.04em;
  line-height: 0.92 !important;
  margin: 0 0 14px !important;
  color: var(--ink) !important;
}

#hero h1 em {
  font-style: italic;
  color: var(--sea-deep);
  background: linear-gradient(120deg, #0b6b64, #1aa6a0 60%, #3b82f6);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

#hero .lede {
  max-width: 28rem;
  margin: 0 auto;
  font-size: clamp(0.95rem, 2.4vw, 1.08rem);
  font-weight: 300;
  line-height: 1.55;
  color: var(--muted);
}

#orbit {
  width: min(220px, 48vw);
  height: min(220px, 48vw);
  margin: 22px auto 8px;
  position: relative;
  animation: floaty 6s ease-in-out infinite;
}

#orbit .ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid rgba(11, 18, 32, 0.08);
}

#orbit .ring:nth-child(2) {
  inset: 18%;
  border-style: dashed;
  animation: spin 28s linear infinite;
}

#orbit .ring:nth-child(3) {
  inset: 36%;
  background:
    radial-gradient(circle at 35% 30%, #ffffff, #e8f7f5 55%, #d7eefc 100%);
  box-shadow:
    inset 0 0 0 1px rgba(255,255,255,0.8),
    0 20px 40px rgba(11, 18, 32, 0.08);
}

#orbit .mark {
  position: absolute;
  inset: 36%;
  display: grid;
  place-items: center;
  font-family: "Instrument Serif", serif;
  font-size: clamp(1.8rem, 5vw, 2.4rem);
  color: var(--ink);
  z-index: 2;
}

/* ===== STAGE ===== */
#stage {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
  animation: rise 0.9s 0.12s cubic-bezier(.22,1,.36,1) both;
}

@media (min-width: 900px) {
  #stage {
    grid-template-columns: 300px 1fr;
    align-items: stretch;
    gap: 18px;
  }
}

/* Side dock — document intake */
#dock {
  background: rgba(255,255,255,0.72);
  border: 1px solid var(--line);
  border-radius: 28px;
  padding: 18px 16px 16px;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 24px 60px rgba(11, 18, 32, 0.06);
}

#dock h3 {
  font-family: "Instrument Serif", serif !important;
  font-size: 1.55rem !important;
  font-weight: 400 !important;
  margin: 0 0 4px !important;
  color: var(--ink) !important;
}

#dock .hint {
  font-size: 0.84rem;
  color: var(--muted);
  line-height: 1.45;
  margin: 0 0 14px;
}

#statusbox textarea {
  background: linear-gradient(135deg, #ecfdf8, #eff6ff) !important;
  border: 1px solid rgba(20, 143, 133, 0.22) !important;
  color: var(--sea-deep) !important;
  border-radius: 14px !important;
  font-weight: 500 !important;
  font-size: 0.86rem !important;
}

.file-preview, .upload-container, [data-testid="file"] {
  border-radius: 18px !important;
  border: 1.5px dashed rgba(20, 143, 133, 0.45) !important;
  background:
    linear-gradient(160deg, rgba(255,255,255,0.95), rgba(236, 253, 245, 0.7)) !important;
  transition: border-color 0.2s ease, transform 0.2s ease !important;
}

.file-preview:hover, .upload-container:hover {
  border-color: var(--sea) !important;
  transform: translateY(-1px);
}

#process-btn {
  width: 100% !important;
  min-height: 48px !important;
  margin-top: 10px !important;
  border-radius: 16px !important;
  font-weight: 600 !important;
  letter-spacing: 0.01em;
  background: linear-gradient(135deg, #0b1220, #1a2a44) !important;
  color: #fff !important;
  border: none !important;
  box-shadow: 0 10px 24px rgba(11, 18, 32, 0.18) !important;
  transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease !important;
}

#process-btn:hover {
  transform: translateY(-2px);
  filter: brightness(1.08);
  box-shadow: 0 14px 28px rgba(20, 143, 133, 0.25) !important;
}

/* Chat theatre */
#theatre {
  display: flex;
  flex-direction: column;
  min-height: 620px;
  background: rgba(255,255,255,0.82);
  border: 1px solid var(--line);
  border-radius: 32px;
  overflow: hidden;
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow:
    0 1px 0 rgba(255,255,255,0.9) inset,
    0 30px 80px rgba(11, 18, 32, 0.08);
}

#theatre-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px 18px;
  border-bottom: 1px solid var(--line);
  background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(248,250,252,0.7));
}

#theatre-top .live {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--ink-soft);
}

#theatre-top .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--sea);
  box-shadow: 0 0 0 0 var(--glow);
  animation: pulse 2.2s ease-out infinite;
}

#chatbot {
  flex: 1;
  background:
    radial-gradient(circle at 100% 0%, rgba(20,143,133,0.05), transparent 40%),
    linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
  border: none !important;
  border-radius: 0 !important;
}

#chatbot .message,
#chatbot [class*="bubble"],
#chatbot .bot,
#chatbot .user {
  animation: bubbleIn 0.35s cubic-bezier(.22,1,.36,1) both;
}

/* Composer bar */
#composer-wrap {
  padding: 12px;
  background: linear-gradient(180deg, rgba(248,250,252,0.4), #ffffff);
  border-top: 1px solid var(--line);
}

#composer-row {
  display: flex;
  gap: 8px;
  align-items: stretch;
  background: var(--mist);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 6px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

#composer-row:focus-within {
  border-color: rgba(20, 143, 133, 0.45);
  box-shadow: 0 0 0 4px var(--glow);
}

#composer textarea {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  min-height: 48px !important;
  font-size: 16px !important;
  padding: 12px 14px !important;
  color: var(--ink) !important;
}

#composer textarea:focus {
  outline: none !important;
  box-shadow: none !important;
}

#send-btn {
  min-width: 108px;
  min-height: 48px !important;
  border-radius: 16px !important;
  font-weight: 600 !important;
  background: linear-gradient(135deg, #148f85, #0b6b64) !important;
  color: #fff !important;
  border: none !important;
  transition: transform 0.18s ease, filter 0.18s ease !important;
}

#send-btn:hover {
  transform: translateY(-1px);
  filter: brightness(1.06);
}

#clear-btn {
  min-width: 72px;
  min-height: 48px !important;
  border-radius: 16px !important;
  background: transparent !important;
  color: var(--muted) !important;
  border: 1px solid transparent !important;
  font-weight: 500 !important;
}

#clear-btn:hover {
  border-color: var(--line) !important;
  background: #fff !important;
  color: var(--ink) !important;
}

button.primary {
  background: #0b1220 !important;
  color: #fff !important;
  border: none !important;
}

/* Motions */
@keyframes heroIn {
  from { opacity: 0; transform: translateY(18px) scale(0.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes rise {
  from { opacity: 0; transform: translateY(22px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes bubbleIn {
  from { opacity: 0; transform: translateY(10px) scale(0.97); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes floaty {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(20, 143, 133, 0.45); }
  70% { box-shadow: 0 0 0 12px rgba(20, 143, 133, 0); }
  100% { box-shadow: 0 0 0 0 rgba(20, 143, 133, 0); }
}

/* Mobile */
@media (max-width: 899px) {
  #hero { padding: 22px 4px 10px; }
  #hero h1 { font-size: clamp(2.8rem, 14vw, 3.8rem) !important; }
  #orbit { margin-top: 12px; }
  #theatre { min-height: 58vh; border-radius: 24px; }
  #dock { border-radius: 22px; }
  #composer-row { flex-wrap: wrap; border-radius: 18px; }
  #composer { flex: 1 1 100%; }
  #send-btn, #clear-btn { flex: 1; }
}

@media (max-width: 480px) {
  .gradio-container { padding: 0 10px 28px !important; }
  #theatre-top { padding: 12px 14px; }
  #composer-wrap { padding: 10px; }
}
"""


HERO_HTML = """
<div id="hero">
  <div class="eyebrow">PDF intelligence</div>
  <h1>Folio<em>.</em></h1>
  <p class="lede">A quiet white studio for document conversations — drop a PDF, then talk to it like a person.</p>
  <div id="orbit" aria-hidden="true">
    <div class="ring"></div>
    <div class="ring"></div>
    <div class="ring"></div>
    <div class="mark">F</div>
  </div>
</div>
"""

THEATRE_TOP = """
<div id="theatre-top">
  <div class="live"><span class="dot"></span> Live session</div>
  <div class="live" style="opacity:.65;font-weight:500;">Ask follow-ups naturally</div>
</div>
"""


def upload_pdf(file):
    from chatbot import process_pdf

    if file is None:
        return "Waiting for a document"

    try:
        path = file if isinstance(file, str) else getattr(file, "name", None)
        if not path:
            return "Could not read that file"
        process_pdf(path)
        return f"Indexed · {os.path.basename(path)}"
    except Exception as exc:
        return f"Failed · {exc}"


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


theme = gr.themes.Base(
    primary_hue=gr.themes.Color(
        c50="#f0fdfa", c100="#ccfbf1", c200="#99f6e4", c300="#5eead4",
        c400="#2dd4bf", c500="#14b8a6", c600="#0d9488", c700="#0f766e",
        c800="#115e59", c900="#134e4a", c950="#042f2e",
    ),
    neutral_hue="slate",
    font=gr.themes.GoogleFont("Sora"),
    font_mono=gr.themes.GoogleFont("IBM Plex Mono"),
).set(
    body_background_fill="#f4f7fb",
    block_background_fill="#ffffff",
    border_color_primary="rgba(11,18,32,0.08)",
    button_primary_background_fill="#0b1220",
    button_primary_background_fill_hover="#148f85",
    button_primary_text_color="#ffffff",
    block_radius="*xl",
    block_shadow="none",
)


with gr.Blocks(title="Folio — PDF Chat", theme=theme, css=CUSTOM_CSS) as demo:
    gr.HTML(HERO_HTML)

    with gr.Row(elem_id="stage", equal_height=True):
        with gr.Column(scale=1, elem_id="dock", min_width=260):
            gr.HTML(
                "<h3>Open a document</h3>"
                "<p class='hint'>Upload any PDF. Folio reads it, then answers only from that file.</p>"
            )
            pdf = gr.File(
                label="PDF file",
                file_types=[".pdf"],
                type="filepath",
                height=120,
            )
            process_btn = gr.Button("Index document", elem_id="process-btn")
            status = gr.Textbox(
                value="Waiting for a document",
                interactive=False,
                show_label=False,
                max_lines=2,
                elem_id="statusbox",
            )

        with gr.Column(scale=2, elem_id="theatre", min_width=300):
            gr.HTML(THEATRE_TOP)
            chatbot = gr.Chatbot(
                show_label=False,
                height=480,
                elem_id="chatbot",
                type="messages",
                bubble_full_width=False,
                placeholder="Once your PDF is indexed, ask anything about it…",
            )
            with gr.Column(elem_id="composer-wrap"):
                with gr.Row(elem_id="composer-row"):
                    msg = gr.Textbox(
                        placeholder="Write a message…",
                        show_label=False,
                        scale=6,
                        elem_id="composer",
                        container=False,
                        autofocus=True,
                    )
                    clear_btn = gr.Button("Clear", elem_id="clear-btn", scale=1)
                    send_btn = gr.Button("Send", elem_id="send-btn", scale=1)

    process_btn.click(upload_pdf, inputs=pdf, outputs=status)
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
