# Plano Detalhado para Trabalho de Visão Computacional - Fase 6

# Plano Detalhado para Trabalho de Visão Computacional - Fase 6

## Contexto e Objetivos do Trabalho


### Objetivo Principal
Desenvolver um sistema de visão computacional utilizando o modelo YOLO (You Only Look Once) que demonstre de forma clara e convincente seu potencial e acurácia na detecção e classificação de objetos escolhidos pelo aluno/grupo.

### Objetivos Específicos
1. Criar, treinar e validar um modelo YOLO customizado para detectar dois tipos de objetos distintos
2. Comparar a performance entre diferentes configurações do modelo (variando épocas de treinamento)
3. Contrastar o modelo YOLO customizado com outras abordagens (YOLO tradicional e CNN treinada do zero)
4. Documentar todo o processo de forma organizada e profissional
5. Demonstrar os resultados obtidos de forma visual e quantitativa

## Entregáveis Detalhados

### Entrega 1: Sistema de Visão Computacional com YOLO Customizado

#### Dataset e Preparação de Dados
- **Dataset Completo:** Organização de banco de imagens contendo no mínimo 40 imagens do objeto A e 40 imagens do objeto B (total mínimo de 80 imagens)
- **Distribuição Adequada:** Para cada objeto, 32 imagens para treinamento, 4 para validação e 4 para testes
- **Organização Estruturada:** Imagens devidamente organizadas em pastas específicas (train, val, test)
- **Rotulação Profissional:** Utilização do Make Sense AI para criar as caixas delimitadoras (bounding boxes) de todos os objetos nas imagens

#### Treinamento e Validação
- **Experimentação Controlada:** Realização de pelo menos dois treinamentos com diferentes números de épocas (recomendado 30 e 60 épocas)
- **Análise Comparativa:** Documentação detalhada das diferenças em acurácia, erro e desempenho entre os modelos treinados com diferentes parâmetros
- **Validação Robusta:** Avaliação completa do modelo utilizando métricas como mAP (mean Average Precision), recall e precision

#### Documentação Técnica
- **Notebook Jupyter/Colab:** Código Python completo, organizado, comentado e totalmente funcional
- **Relatório Analítico:** Células markdown explicando cada etapa do processo e discorrendo sobre resultados obtidos
- **Evidências Visuais:** Prints de imagens de teste processadas pelo modelo, demonstrando sua eficácia
- **Conclusões Fundamentadas:** Análise crítica dos pontos fortes e limitações do modelo

#### Repositório e Apresentação
- **Repositório GitHub:** Criação de repositório contendo todos os arquivos do projeto, incluindo notebook Jupyter
- **README Detalhado:** Documentação introdutória conduzindo o leitor para o notebook Jupyter
- **Vídeo Demonstrativo:** Gravação de vídeo de até 5 minutos demonstrando o funcionamento do sistema

### Entrega 2: Análise Comparativa de Abordagens

#### Implementação de Diferentes Abordagens
- **YOLO Tradicional:** Aplicação do modelo YOLO pré-treinado (sem customização) no mesmo conjunto de dados
- **CNN do Zero:** Desenvolvimento de uma rede neural convolucional treinada do zero para o mesmo problema

#### Análise Técnica Comparativa
- **Facilidade de Uso:** Avaliação da complexidade de implementação e integração de cada abordagem
- **Precisão dos Modelos:** Comparação detalhada das métricas de desempenho (acurácia, precisão, recall)
- **Eficiência de Treinamento:** Análise do tempo necessário para treinamento e customização de cada modelo
- **Performance de Inferência:** Medição do tempo de predição (inferência) para cada abordagem

#### Documentação e Entregáveis
- **Notebook Complementar:** Implementação documentada das abordagens alternativas
- **Visualizações Comparativas:** Gráficos e tabelas comparando o desempenho das diferentes soluções
- **Análise Crítica:** Avaliação das vantagens e desvantagens de cada método em cenários práticos

## Plano de Execução - Passo a Passo

### Fase 0: Preparação do Ambiente (Setup Inicial)

1. **Verificar instalações atuais e atualizar pacotes:**
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Instalar pacotes necessários para o projeto:**
   ```bash
   pip install numpy matplotlib opencv-python torch torchvision tensorflow scikit-learn pandas pillow
   ```

3. **Instalar o Ultralytics YOLO (implementação open-source do YOLOv5):**
   ```bash
   pip install ultralytics
   ```

4. **Configurar o Jupyter Notebook no VS Code:**
   - Verificar se a extensão Jupyter do VS Code está ativa
   - Criar uma pasta dedicada para o projeto
   - Iniciar um novo notebook `.ipynb` dentro desta pasta

### Fase 1: Coleta e Preparação de Dados

1. **Escolha dos objetos a serem detectados:**
   - Selecionar dois objetos bem diferentes entre si (exemplo: "Xícara" e "Livro")
   - Os objetos devem ser facilmente fotografáveis e terem características distintas

2. **Fontes para obtenção das imagens:**
   - **Opção 1 - Captura própria:** Usar câmera do celular ou webcam para capturar 40 imagens de cada objeto em diferentes ângulos, iluminações e fundos
   - **Opção 2 - Bancos de imagens gratuitos:**
     - [Unsplash](https://unsplash.com/) 
     - [Pexels](https://www.pexels.com/)
     - [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)
     - [COCO Dataset](https://cocodataset.org/#home)
   - **Opção 3 - Datasets já organizados:**
     - [Roboflow Universe](https://universe.roboflow.com/) (datasets prontos para YOLO)
     - [Kaggle Datasets](https://www.kaggle.com/datasets)

3. **Organização das imagens:**
   - Criar uma estrutura de pastas no seu computador:
     ```
     dataset/
     ├── objeto_A/
     │   ├── train/ (32 imagens)
     │   ├── val/ (4 imagens)
     │   └── test/ (4 imagens)
     └── objeto_B/
         ├── train/ (32 imagens)
         ├── val/ (4 imagens)
         └── test/ (4 imagens)
     ```
   - Renomear as imagens de forma organizada (ex: "objeto_A_001.jpg")
   - Redimensionar as imagens para um tamanho padrão se necessário (ex: 640x640)

### Fase 2: Anotação e Rotulagem de Dados

1. **Preparar arquivos para rotulação:**
   - Organizar as imagens de treino e validação para upload no Make Sense AI

2. **Processo de rotulação usando Make Sense AI:**
   - Acessar [Make Sense AI](https://www.makesense.ai/)
   - Selecionar a opção "Object Detection"
   - Fazer upload das imagens de treino e validação
   - Criar labels para os objetos A e B
   - Desenhar caixas delimitadoras (bounding boxes) em torno dos objetos em cada imagem
   - Exportar as anotações no formato YOLO

3. **Organização dos arquivos de anotação:**
   - Criar diretórios para os labels correspondentes às imagens:
     ```
     labels/
     ├── train/
     └── val/
     ```
   - Armazenar os arquivos .txt exportados nas pastas correspondentes

### Fase 3: Treinamento e Validação do Modelo YOLO

1. **Criação do arquivo de configuração do dataset:**
   - Criar um arquivo `data.yaml` com informações do dataset:
     ```yaml
     train: path/to/train
     val: path/to/val
     nc: 2  # número de classes
     names: ['Objeto_A', 'Objeto_B']  # nomes das classes
     ```

2. **Preparação do notebook para treinamento:**
   - Importar bibliotecas necessárias
   - Definir caminhos para pastas e arquivos
   - Configurar hiperparâmetros do treinamento

3. **Treinamento do modelo com diferentes épocas:**
   - Realizar primeiro treinamento com 30 épocas
   - Realizar segundo treinamento com 60 épocas
   - Salvar os pesos dos modelos treinados (arquivos .pt)

4. **Validação do modelo:**
   - Avaliar a performance do modelo em cada configuração
   - Analisar métricas como mAP (mean Average Precision), recall e precision
   - Comparar os resultados entre as diferentes configurações
   - Gerar visualizações das previsões

### Fase 4: Teste do Modelo

1. **Teste com imagens separadas:**
   - Utilizar as imagens de teste que não foram usadas no treinamento
   - Executar o modelo treinado nestas imagens
   - Salvar os resultados visuais (imagens com bounding boxes)

2. **Análise de desempenho:**
   - Calcular métricas de precisão para o conjunto de teste
   - Identificar falsos positivos, falsos negativos e casos de sucesso
   - Documentar as limitações observadas

### Fase 5: Implementação de Abordagens Alternativas (Entrega 2)

1. **Aplicação da YOLO tradicional:**
   - Utilizar o modelo YOLOv5 pré-treinado sem customização
   - Avaliar a performance no mesmo conjunto de dados
   - Comparar com o modelo customizado

2. **Treinamento de uma CNN do zero:**
   - Criar uma arquitetura CNN simples usando PyTorch ou TensorFlow
   - Treinar a CNN no mesmo conjunto de dados (adaptando para classificação)
   - Avaliar a performance e comparar com as abordagens YOLO

3. **Análise comparativa:**
   - Criar tabelas e gráficos para comparação de performance
   - Avaliar tempo de treinamento, acurácia e outros parâmetros relevantes
   - Documentar vantagens e desvantagens de cada abordagem

### Fase 6: Documentação e Finalização

1. **Organização do notebook:**
   - Garantir que o código esteja organizado e comentado
   - Adicionar células markdown explicando cada etapa
   - Incluir visualizações e gráficos relevantes
   - Documentar as conclusões sobre os experimentos

2. **Criação do repositório no GitHub:**
   - Inicializar um repositório com nome adequado
   - Fazer upload do notebook e arquivos relevantes
   - Criar um README.md detalhado explicando o projeto

3. **Gravação do vídeo demonstrativo:**
   - Preparar um roteiro para o vídeo de 5 minutos
   - Demonstrar o funcionamento do sistema
   - Explicar brevemente a implementação e resultados
   - Fazer upload no YouTube como "não listado"
   - Adicionar o link do vídeo ao README do GitHub

## Lista de Materiais Necessários

### Software:
- Python 3.9 (já instalado)
- VS Code com extensão Jupyter (já instalado)
- Bibliotecas Python:
  - numpy, matplotlib, opencv-python
  - torch, torchvision
  - tensorflow/keras
  - scikit-learn
  - ultralytics (para YOLO)
  - pandas, pillow

### Hardware:
- Computador com capacidade para processamento de imagens (CPU ou GPU)
- Câmera para captura de imagens (opcional - celular ou webcam)

### Recursos Online:
- Conta no GitHub para hospedagem do código
- Conta no Google Drive para backup (opcional)
- Serviço Make Sense AI para rotulação
- Conta no YouTube para upload do vídeo demonstrativo

## Estrutura Completa do Projeto

```
projeto_visao_computacional/
├── dataset/
│   ├── objeto_A/
│   │   ├── train/ (32 imagens)
│   │   ├── val/ (4 imagens)
│   │   └── test/ (4 imagens)
│   └── objeto_B/
│       ├── train/ (32 imagens)
│       ├── val/ (4 imagens)
│       └── test/ (4 imagens)
│
├── labels/
│   ├── train/ (arquivos de anotação para imagens de treino)
│   └── val/ (arquivos de anotação para imagens de validação)
│
├── models/ (para salvar os modelos treinados)
│   ├── model_30epochs.pt
│   └── model_60epochs.pt
│
├── results/ (para salvar resultados visuais e métricas)
│   ├── yolo_custom/
│   ├── yolo_traditional/
│   └── cnn/
│
├── notebooks/
│   ├── nome_RM_pbl_fase6.ipynb (notebook principal)
│   └── notebooks_auxiliares/ (se necessário)
│
├── config/
│   └── data.yaml (configuração do dataset para YOLO)
│
├── docs/ (documentação adicional)
│
├── README.md (documentação principal do projeto)
├── requirements.txt (dependências do projeto)
└── .gitignore (para arquivos grandes, temporários, etc.)
```

Esta estrutura organiza claramente:
- Dados de entrada (dataset)
- Anotações (labels)
- Modelos treinados (models)
- Resultados gerados (results)
- Código (notebooks)
- Configurações (config)
- Documentação (docs e README.md)

