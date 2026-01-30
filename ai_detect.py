from ultralytics import YOLO

# Carrega o modelo de IA (ele vai baixar o arquivo yolov8n.pt sozinho na primeira vez)
model = YOLO("yolov8n.pt")

# Manda a IA olhar para uma imagem e identificar o que tem nela
# Vou usar uma foto de um ônibus e pessoas de exemplo
results = model.predict("https://ultralytics.com/images/bus.jpg", save=True )

print("SUCESSO! A IA analisou a imagem.")
print("Olhe na pasta 'runs/detect/predict' para ver o resultado com os quadrados!")
