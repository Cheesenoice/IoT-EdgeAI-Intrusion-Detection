# ============================================================
# SENTINEL EYE - Script Đánh Giá và So Sánh Model YOLOv8
# Chạy: python evaluate.py
# Yêu cầu: ultralytics (pip install ultralytics)
# ============================================================

import os
import sys

def main():
    try:
        from ultralytics import YOLO
    except ImportError:
        print("❌ Chưa cài đặt thư viện 'ultralytics'. Chạy lệnh: pip install ultralytics")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_yaml = os.path.join(base_dir, "dataset", "data.yaml")
    base_model_path = os.path.join(base_dir, "..", "server", "yolov8n.pt")
    custom_model_path = os.path.join(base_dir, "..", "server", "sentinel_eye.pt")

    print("=" * 60)
    print("  SENTINEL EYE - Đánh Giá Model YOLOv8")
    print("=" * 60)

    if not os.path.exists(data_yaml):
        print(f"❌ Không tìm thấy cấu hình dataset: {data_yaml}")
        return

    # 1. Đánh giá model gốc
    if os.path.exists(base_model_path):
        print(f"\n[1/2] Đang đánh giá model gốc ({base_model_path})...")
        try:
            base_model = YOLO(base_model_path)
            metrics_base = base_model.val(data=data_yaml)
            print(f"  Base Model mAP50:    {metrics_base.box.map50:.4f}")
            print(f"  Base Model mAP50-95: {metrics_base.box.map:.4f}")
        except Exception as e:
            print(f"  ⚠️ Lỗi khi đánh giá model gốc: {e}")
    else:
        print(f"\n⚠️ Không tìm thấy model gốc: {base_model_path}")

    # 2. Đánh giá model fine-tuned
    if os.path.exists(custom_model_path):
        print(f"\n[2/2] Đang đánh giá model fine-tuned ({custom_model_path})...")
        try:
            custom_model = YOLO(custom_model_path)
            metrics_custom = custom_model.val(data=data_yaml)
            print(f"  Fine-tuned mAP50:    {metrics_custom.box.map50:.4f}")
            print(f"  Fine-tuned mAP50-95: {metrics_custom.box.map:.4f}")
        except Exception as e:
            print(f"  ⚠️ Lỗi khi đánh giá model fine-tuned: {e}")
    else:
        print(f"\n⚠️ Chưa có model fine-tuned: {custom_model_path}")

    print("\n" + "=" * 60)
    print("Hoàn tất đánh giá!")
    print("=" * 60)

if __name__ == "__main__":
    main()
