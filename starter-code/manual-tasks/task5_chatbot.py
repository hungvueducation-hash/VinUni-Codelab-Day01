"""
Chạy thử riêng Task 5 — streaming_chatbot.

Cách chạy (từ thư mục VinUni_Codelab_Day01_Template):
    py starter-code\\manual-tasks\\task5_chatbot.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from template import streaming_chatbot

if __name__ == "__main__":
    print("=== Gemini Chatbot (gõ 'quit' hoặc 'exit' để thoát) ===")
    try:
        streaming_chatbot()
    except Exception as e:
        print(f"Lỗi: {e}")
