"""
Chạy thử riêng Task 1 — call_openai.

Cách chạy (từ thư mục VinUni_Codelab_Day01_Template):
    py starter-code\\manual-tasks\\task1_openai.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from template import call_openai

if __name__ == "__main__":
    prompt = "Hãy giải thích sự khác biệt giữa temperature và top_p bằng tiếng Việt ngắn gọn trong 2 câu."
    try:
        text, latency, usage = call_openai(prompt)
        print(f"Latency: {latency:.2f}s")
        print(f"Tokens: {usage['input_tokens']} in / {usage['output_tokens']} out")
        print(f"Response: {text}")
    except Exception as e:
        print(f"Lỗi: {e}")
