import os
import shutil
from glob import glob

# Pastas principais
splits = ["train", "valid", "test"]
base_dir = "projeto_visao_computacional/dataset"

# Subpastas de origem (corrigidas)
origens = [
    "objeto_a_copo",
    "objeto_b_headphones"
]

def limpa_pasta(pasta):
    if os.path.exists(pasta):
        for arquivo in os.listdir(pasta):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                os.remove(caminho)
            elif os.path.isdir(caminho):
                shutil.rmtree(caminho)

def copia_arquivos(origem, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)
    for arquivo in glob(os.path.join(origem, "*")):
        shutil.copy2(arquivo, destino)

def reorganiza():
    for split in splits:
        # Limpa pastas gerais
        images_dir = os.path.join(base_dir, split, "images")
        labels_dir = os.path.join(base_dir, split, "labels")
        limpa_pasta(images_dir)
        limpa_pasta(labels_dir)
        os.makedirs(images_dir, exist_ok=True)
        os.makedirs(labels_dir, exist_ok=True)
        # Copia arquivos validados das subpastas
        for origem in origens:
            origem_images = os.path.join(base_dir, origem, split, "images")
            origem_labels = os.path.join(base_dir, origem, split, "labels")
            if os.path.exists(origem_images):
                copia_arquivos(origem_images, images_dir)
            if os.path.exists(origem_labels):
                copia_arquivos(origem_labels, labels_dir)
    print("Reorganização concluída.")

if __name__ == "__main__":
    reorganiza()
