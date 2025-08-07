import asyncio
from rag import get_rag_response
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# 🎯 Test seti
test_set = [
    {"question": "What do polar bears eat?", "expected_answer": "seals"},
    {"question": "How do polar bears stay warm in the Arctic?", "expected_answer": "Thick fur and a fat layer up to 4.5 inches thick"},
    {"question": "Where do polar bears live?", "expected_answer": "Arctic"},
    {"question": "Why are polar bear paws large?", "expected_answer": "To help them walk on ice and swim across water"},
    {"question": "How thick can a polar bear's fat layer be?", "expected_answer": "up to 4.5 inches"},
]

# ✅ Basit benzerlik eşik kontrolü
def is_similar(answer, expected, threshold=0.5):
    vect = TfidfVectorizer().fit([answer, expected])
    vecs = vect.transform([answer, expected])
    sim = (vecs[0] @ vecs[1].T).toarray()[0][0]
    return sim >= threshold

# 🔍 Değerlendirme
async def evaluate():
    y_true = []
    y_pred = []

    for item in test_set:
        question = item["question"]
        expected = item["expected_answer"]

        try:
            predicted = await get_rag_response(question)
        except Exception as e:
            predicted = ""
            print(f"[!] Error for question: {question} -> {e}")

        match = is_similar(predicted.lower(), expected.lower())
        y_true.append(1)
        y_pred.append(1 if match else 0)

        status = "✅" if match else "❌"
        print(f"{status} Q: {question}")
        print(f"    Expected: {expected}")
        print(f"    Got     : {predicted}\n")

    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print("📊 Evaluation Metrics")
    print(f"Precision: {precision:.2f}")
    print(f"Recall   : {recall:.2f}")
    print(f"F1 Score : {f1:.2f}")

# ▶️ Başlat
if __name__ == "__main__":
    asyncio.run(evaluate())
