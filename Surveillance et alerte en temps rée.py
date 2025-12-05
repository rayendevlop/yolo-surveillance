import cv2
from ultralytics import YOLO
import time
import os

# Créer un dossier pour sauvegarder les captures
SAVE_DIR = "detections"
os.makedirs(SAVE_DIR, exist_ok=True)

# Charger modèle YOLOv8
model = YOLO("yolov8n.pt")  # modèle nano, léger et rapide

# Ouvrir caméra
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection
    results = model(frame)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if conf > 0.5 and cls == 0:  # 0 = personne
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
                cv2.putText(frame, f"Personne {conf:.2f}", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
                
                # Sauvegarder image
                filename = os.path.join(SAVE_DIR, f"detection_{int(time.time())}.jpg")
                cv2.imwrite(filename, frame)
                
                # Son d'alerte sur Mac
                os.system("afplay alert.mp3")  # place alert.mp3 dans le même dossier

    # Afficher la vidéo
    cv2.imshow("Surveillance IA", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
