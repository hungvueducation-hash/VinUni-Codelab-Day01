"""
Chạy thử riêng Bonus B — batch_compare.

Cách chạy (từ thư mục VinUni_Codelab_Day01_Template):
    py starter-code\\manual-tasks\\bonusB_batch.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from template import batch_compare

if __name__ == "__main__":
    prompts = [
        "Giải thích AI là gì trong 1 câu.",
        "Giải thích Machine Learning là gì trong 1 câu.",
    ]
    try:
        results = batch_compare(prompts)
        for r in results:
            print(f"\n=== Prompt: {r['prompt']} ===")
            for model_name in ("gpt4o", "gpt4o_mini", "gemini_flash"):
                stats = r[model_name]
                print(f"[{model_name}] cost=${stats['cost']:.6f} latency={stats['latency']:.2f}s")
    except Exception as e:
        print(f"Lỗi: {e}")
