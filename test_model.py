from ultralytics import YOLO

model = YOLO("models/best.pt")

print("Classes:", model.names)

results = model("knife.jpg", conf=0.10, save=True)

for r in results:
    print(r.boxes)