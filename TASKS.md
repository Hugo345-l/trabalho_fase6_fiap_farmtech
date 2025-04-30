# Checklist de Tarefas - Projeto de Visão Computacional YOLO

Este documento contém uma lista de verificação de todas as tarefas necessárias para completar o projeto de visão computacional da Fase 6. Marque as caixas conforme você completa cada tarefa.

## Fase 0: Preparação do Ambiente

- [x] Atualizar pip para a versão mais recente
- [x] Instalar pacotes básicos (numpy, matplotlib, opencv-python)
- [x] Instalar frameworks de deep learning (torch, torchvision, tensorflow)
- [x] Instalar bibliotecas auxiliares (scikit-learn, pandas, pillow)
- [x] Instalar Ultralytics YOLO
- [x] Verificar a extensão Jupyter no VS Code
- [x] Criar pasta dedicada para o projeto
- [x] Iniciar notebook .ipynb para o projeto

## Fase 1: Coleta e Preparação de Dados

- [x] Definir os dois objetos a serem detectados
- [x] Planejar a captura/coleta de imagens
- [x] Obter 40 imagens do objeto A
- [x] Obter 40 imagens do objeto B
- [x] Criar estrutura de pastas para o dataset
- [x] Separar imagens do objeto A (32 treino, 4 validação, 4 teste)
- [x] Separar imagens do objeto B (32 treino, 4 validação, 4 teste) 
- [x] Reduzir dataset para 40 treino, 5 validação e 5 teste por classe (validado correspondência imagem/label)
- [x] Redimensionar imagens se necessário
- [x] Verificar a qualidade das imagens

## Fase 2: Anotação e Rotulagem

- [x] Criar labels para os objetos A e B
- [x] Desenhar bounding boxes em imagens de treino
- [x] Desenhar bounding boxes em imagens de validação
- [x] Organizar arquivos de label nas pastas correspondentes
- [x] Exportar anotações no formato YOLO
- [x] Criar diretórios para os labels

## Fase 3: Treinamento e Validação

- [x] Criar arquivo de configuração data.yaml
- [ ] Configurar caminhos para diretórios de treino e validação no yaml
- [ ] Definir nomes das classes no arquivo yaml
- [ ] Criar células no notebook para importar bibliotecas
- [ ] Configurar caminhos para os arquivos no notebook
- [ ] Definir hiperparâmetros para o treinamento
- [ ] Executar primeiro treinamento (30 épocas)
- [ ] Salvar pesos do primeiro treinamento
- [ ] Executar segundo treinamento (60 épocas)
- [ ] Salvar pesos do segundo treinamento
- [ ] Calcular métricas para o primeiro modelo
- [ ] Calcular métricas para o segundo modelo
- [ ] Gerar visualizações das previsões
- [ ] Documentar resultados da validação

## Fase 4: Teste do Modelo

- [ ] Preparar as imagens de teste
- [ ] Executar modelo com 30 épocas nas imagens de teste
- [ ] Executar modelo com 60 épocas nas imagens de teste
- [ ] Salvar resultados visuais (imagens com bounding boxes)
- [ ] Calcular métricas de precisão para o conjunto de teste
- [ ] Identificar falsos positivos e falsos negativos
- [ ] Documentar casos de sucesso
- [ ] Listar limitações observadas no modelo

## Fase 5: Abordagens Alternativas

- [ ] Preparar YOLO tradicional (pré-treinado)
- [ ] Executar YOLO tradicional no conjunto de dados
- [ ] Calcular métricas do YOLO tradicional
- [ ] Implementar uma arquitetura CNN do zero
- [ ] Adaptar o dataset para formato de classificação
- [ ] Treinar a CNN do zero
- [ ] Calcular métricas da CNN
- [ ] Criar tabela comparativa de performance
- [ ] Gerar gráficos comparativos
- [ ] Analisar tempo de treinamento de cada abordagem
- [ ] Documentar vantagens e desvantagens de cada método

## Fase 6: Documentação e Finalização

- [ ] Organizar e comentar o código
- [ ] Adicionar células markdown com explicações
- [ ] Incluir visualizações e gráficos nos notebooks
- [ ] Documentar conclusões dos experimentos
- [ ] Criar repositório no GitHub
- [ ] Fazer upload do notebook e arquivos relevantes
- [x] Escrever README.md detalhado
- [ ] Preparar roteiro para o vídeo demonstrativo
- [ ] Gravar vídeo de 5 minutos
- [ ] Fazer upload do vídeo no YouTube como "não listado"
- [ ] Adicionar link do vídeo ao README
- [ ] Verificar todos os requisitos do barema de avaliação
- [ ] Fazer backup de todos os arquivos e dados

## Preparação da Entrega Final

- [ ] Verificar o nome correto do arquivo (nome_RM_pbl_fase6.ipynb)
- [ ] Conferir se o repositório está público
- [ ] Confirmar se as células do notebook foram todas executadas
- [ ] Verificar se o link do vídeo está funcionando
- [ ] Finalizar e enviar o link do GitHub pelo portal da FIAP
