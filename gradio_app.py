
import gradio as gr
from rag import get_rag_response
import asyncio

def ask_question(query):
    try:
        return asyncio.run(get_rag_response(query))
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

with gr.Blocks(title="🐻‍❄️ Polar Bear QA System") as demo:
    gr.Markdown("### 🐻‍❄️ Polar Bear QA\nBelgeye dayalı olarak kutup ayıları hakkında sorular sorabilirsiniz.")
    
    with gr.Row():
        query = gr.Textbox(label="Soru", placeholder="Kutup ayıları ne yer?", lines=2)
    
    output = gr.Textbox(label="Yanıt", lines=4, interactive=False)
    
    submit = gr.Button("Cevapla")
    submit.click(fn=ask_question, inputs=query, outputs=output)

if __name__ == "__main__":
    demo.launch()
