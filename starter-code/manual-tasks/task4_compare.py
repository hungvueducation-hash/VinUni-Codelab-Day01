"""
Chạy thử riêng Task 4 — compare_models.

Cách chạy (từ thư mục VinUni_Codelab_Day01_Template):
    py starter-code\\manual-tasks\\task4_compare.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from template import compare_models

if __name__ == "__main__":
    prompt = "Hãy giải thích sự khác biệt giữa temperature và top_p bằng tiếng Việt ngắn gọn trong 2 câu."
    try:
        result = compare_models(prompt)
        for model_name, stats in result.items():
            print(f"\n[{model_name.upper()}]")
            print(f"Latency: {stats['latency']:.2f}s | Cost: ${stats['cost']:.6f}")
            print(f"Tokens: {stats['input_tokens']} in / {stats['output_tokens']} out")
            print(f"Response: {stats['response']}")
    except Exception as e:
        print(f"Lỗi: {e}")
