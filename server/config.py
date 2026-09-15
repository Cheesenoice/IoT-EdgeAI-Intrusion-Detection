# ============================================================
# SENTINEL EYE - Configuration
# ============================================================

import os
try:
    from dotenv import load_dotenv
    # Load .env from server directory if available
    _env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.exists(_env_path):
        load_dotenv(_env_path)
    else:
        load_dotenv()
except ImportError:
    pass

# ESP32-CAM Settings
# Thay đổi IP này cho đúng với IP của ESP32-CAM (xem trên Serial Monitor hoặc đặt trong .env)
ESP32_IP = os.getenv("ESP32_IP", "192.168.16.75")
ESP32_STREAM_URL = f"http://{ESP32_IP}/stream"
ESP32_CAPTURE_URL = f"http://{ESP32_IP}/capture"
ESP32_BUZZER_ON_URL = f"http://{ESP32_IP}:81/buzzer/on"
ESP32_BUZZER_OFF_URL = f"http://{ESP32_IP}:81/buzzer/off"
ESP32_STATUS_URL = f"http://{ESP32_IP}/status"

# Flask Server Settings
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", "5000"))
DEBUG_MODE = os.getenv("DEBUG_MODE", "True").lower() in ("true", "1", "t", "yes")

# Intrusion Log Settings
LOG_DIR = os.getenv("LOG_DIR", "intrusion_logs")
MAX_LOG_IMAGES = int(os.getenv("MAX_LOG_IMAGES", "500"))  # Giữ tối đa bao nhiêu ảnh log

# Alert Settings
ALERT_COOLDOWN_SECONDS = int(os.getenv("ALERT_COOLDOWN_SECONDS", "30"))  # Thời gian tối thiểu giữa 2 lần cảnh báo (30s)
BUZZER_DURATION_SECONDS = int(os.getenv("BUZZER_DURATION_SECONDS", "3"))  # Thời gian còi kêu mỗi lần

# Burst Capture Settings (Chụp liên tục khi phát hiện xâm nhập)
BURST_CAPTURE_COUNT = int(os.getenv("BURST_CAPTURE_COUNT", "5"))          # Số ảnh chụp mỗi lần cảnh báo
BURST_CAPTURE_INTERVAL = int(os.getenv("BURST_CAPTURE_INTERVAL", "1"))   # Khoảng cách giữa mỗi ảnh (giây) → 5 ảnh × 1s = 5 giây

# ===================== YOLO SETTINGS (DUAL MODEL) =====================
# Model 1: Phát hiện TẤT CẢ người (pre-trained COCO)
YOLO_MODEL = os.getenv("YOLO_MODEL", "yolov8n.pt")
YOLO_CONFIDENCE = float(os.getenv("YOLO_CONFIDENCE", "0.45"))           # Ngưỡng tin cậy (0.0 - 1.0)
YOLO_PERSON_CLASS_ID = int(os.getenv("YOLO_PERSON_CLASS_ID", "0"))      # Class ID 0 = "person" trong COCO dataset
YOLO_DETECT_INTERVAL = int(os.getenv("YOLO_DETECT_INTERVAL", "2"))      # Chạy YOLO mỗi N frame

# Model 2: Nhận diện CHỦ NHÀ (fine-tuned)
OWNER_MODEL = os.getenv("OWNER_MODEL", "sentinel_eye.pt")               # Model đã train nhận diện chủ nhà
OWNER_CONFIDENCE = float(os.getenv("OWNER_CONFIDENCE", "0.82"))         # Ngưỡng tin cậy nhận diện chủ nhà
OWNER_DETECT_ENABLED = os.getenv("OWNER_DETECT_ENABLED", "True").lower() in ("true", "1", "t", "yes")

# ===================== DISTANCE ESTIMATION =====================
# Công thức: Khoảng cách = (H_thuc * F) / h_pixel
KNOWN_PERSON_HEIGHT_M = float(os.getenv("KNOWN_PERSON_HEIGHT_M", "1.65"))     # Chiều cao trung bình người Việt Nam (M)
# Tạm thời để FOCAL_LENGTH (Tiêu cự) = 500. Bạn cần đứng cách camera đúng 2 mét, đo xem box cao bao nhiêu pixel
# FOCAL_LENGTH = (h_pixel_thực_đo * 2.0 mét) / 1.65 mét
FOCAL_LENGTH = float(os.getenv("FOCAL_LENGTH", "500.0"))

# ===================== EMAIL ALERT =====================
EMAIL_ALERT_ENABLED = os.getenv("EMAIL_ALERT_ENABLED", "True").lower() in ("true", "1", "t", "yes")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "your_gmail_app_password")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "receiver_email@gmail.com")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
