# Detecção de Objetos com YOLOv8

Este repositório contém uma implementação inicial de visão computacional utilizando o modelo YOLOv8 da Ultralytics. O objetivo deste projeto é realizar testes práticos de identificação de objetos em imagens estáticas.

## Descrição do Projeto

O script desenvolvido utiliza a arquitetura YOLOv8 (You Only Look Once) para processar imagens e identificar classes específicas como pessoas, veículos e sinalizações de trânsito. O modelo utilizado é o yolov8n (nano), escolhido pelo equilíbrio entre velocidade de processamento e precisão.

## Arquivos do Repositório

- **ai_detect.py**: Script Python responsável por carregar o modelo e realizar a inferência na imagem.
- **bus.jpg**: Resultado da detecção processada, contendo as caixas delimitadoras (bounding boxes) e as classes identificadas.
- **yolov8n.pt**: Pesos do modelo pré-treinado utilizado na execução.

## Requisitos e Instalação

Para executar este projeto localmente, é necessário ter o Python instalado e a biblioteca ultralytics configurada.

1. Instalação da dependência principal:
   pip install ultralytics

2. Execução do script:
   python ai_detect.py

## Resultados

Após a execução, o script gera automaticamente uma pasta de saída em 'runs/detect/predict' contendo as imagens analisadas com as marcações de detecção em tempo real

---
Desenvolvido como parte de estudos em Inteligência Artificial e Visão Computacional.
