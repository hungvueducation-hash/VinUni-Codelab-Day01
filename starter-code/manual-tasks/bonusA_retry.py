"""
Chạy thử riêng Bonus A — retry_with_backoff (không cần API key, demo bằng hàm giả lập lỗi).

Cách chạy (từ thư mục VinUni_Codelab_Day01_Template):
    py starter-code\\manual-tasks\\bonusA_retry.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from template import retry_with_backoff

if __name__ == "__main__":
    state = {"attempts": 0}

    def flaky_fn():
        state["attempts"] += 1
        print(f"  thử lần {state['attempts']}...")
        if state["attempts"] < 3:
            raise ValueError("Giả lập lỗi tạm thời")
        return "Thành công!"

    try:
        result = retry_with_backoff(flaky_fn, max_retries=3, base_delay=0.3)
        print(f"Kết quả: {result}")
    except Exception as e:
        print(f"Thất bại sau khi retry: {e}")
