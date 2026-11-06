"""
Chạy thử riêng Bonus C — format_comparison_table (dùng dữ liệu giả lập, không cần API key).

Cách chạy (từ thư mục VinUni_Codelab_Day01_Template):
    py starter-code\\manual-tasks\\bonusC_table.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from template import format_comparison_table

if __name__ == "__main__":
    fake_results = [
        {
            "prompt": "Q1",
            "gpt4o": {"response": "GPT-4o response content here", "latency": 0.5, "cost": 0.00045, "input_tokens": 10, "output_tokens": 20},
            "gpt4o_mini": {"response": "GPT-4o-Mini response content here", "latency": 0.3, "cost": 0.0000135, "input_tokens": 10, "output_tokens": 20},
            "gemini_flash": {"response": "Gemini response content here", "latency": 0.4, "cost": 0.00000675, "input_tokens": 10, "output_tokens": 20},
        },
    ]
    table = format_comparison_table(fake_results)
    print(table)
