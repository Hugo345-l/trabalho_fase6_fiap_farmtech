# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/"><img src="../assets/logo-fiap%20(1).png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

<br>

# Projeto Visão Computacional

## 👨‍🎓 Integrantes
- <a href="https://www.linkedin.com/in/bruno-castro-dias/">Bruno Castro - RM558359</a>
- <a href="https://www.linkedin.com/in/hugomariano191628150/">Hugo Mariano - RM560688</a>
- <a href="https://www.linkedin.com/in/matheus-castro-63644b224/">Matheus Castro - RM559293</a>

## 📜 Descrição

Este projeto tem como objetivo aplicar técnicas de visão computacional para detecção automática de objetos em imagens, utilizando modelos baseados em YOLO. O foco está na organização eficiente dos datasets, treinamento e avaliação de modelos para identificar diferentes classes de objetos (ex: copos de café, headphones), promovendo reprodutibilidade e expansão futura para novas classes.

O projeto foi desenvolvido como parte do curso de Engenharia de Software da FIAP, integrando conceitos de machine learning, manipulação de dados e boas práticas de organização de projetos de ciência de dados.

## 📁 Mapa de Pastas

- <b>dataset/</b>: Conjunto de dados para detecção de objetos, organizado por classes e splits (train/valid/test).
- <b>config/</b>: Arquivos de configuração do projeto (ex: data.yaml).
- <b>models/</b>: Modelos treinados e arquivos relacionados.
- <b>notebooks/</b>: Jupyter Notebooks com experimentos, análises e o notebook final do projeto.
- <b>assets/</b>: Imagens e recursos visuais do projeto.
- <b>PLANNING.md</b>: Planejamento e decisões do projeto.
- <b>TASKS.md</b>: Quadro de tarefas e pendências.
- <b>requirements.txt</b>: Dependências do projeto.
- <b>reduz_dataset.py</b>, <b>verifica_correspondencia_labels.py</b>, <b>verifica_dimensoes.py</b>: Scripts utilitários para manipulação e verificação dos dados.

> 📓 <b>Notebook final:</b> <a href="notebooks/HugoMariano_rm560688_pbl_fase6.ipynb">notebooks/HugoMariano_rm560688_pbl_fase6.ipynb</a>

## 🔧 Como executar

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
2. Execute os notebooks ou scripts conforme a necessidade.
3. Para treinar modelos, utilize os dados organizados em `dataset/` e siga as instruções nos notebooks.

## 🗃 Histórico de versões

- 1.0 - 30/04/2025

## 📋 Licença

Este projeto segue o modelo educacional FIAP e está licenciado sob Creative Commons Attribution 4.0 International.
