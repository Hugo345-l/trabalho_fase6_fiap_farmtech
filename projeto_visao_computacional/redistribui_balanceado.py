import os
import shutil
import random

base_dir = "projeto_visao_computacional/dataset"
splits = {"train": 40, "val": 5, "test": 5}
classes = [
    ("objeto_a_copo", 0),
    ("objeto_b_headphones", 1)
]

def limpa_pasta(pasta):
    if os.path.exists(pasta):
        for arquivo in os.listdir(pasta):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                os.remove(caminho)
            elif os.path.isdir(caminho):
                shutil.rmtree(caminho)

def copia_amostras_exclusivas(classe_dir, classe_idx):
    # Junta todas as imagens disponíveis para a classe, removendo duplicatas pelo nome do arquivo
    imagens_dict = {}
    for split_src in ["train", "valid", "test"]:
        images_src = os.path.join(base_dir, classe_dir, split_src, "images")
        if os.path.exists(images_src):
            for f in os.listdir(images_src):
                if f.endswith(".jpg"):
                    imagens_dict[f] = os.path.join(images_src, f)
    imagens = list(imagens_dict.values())
    random.shuffle(imagens)
    # Divide para cada split, respeitando o limite de cada um
    idx = 0
    for split, qtd in splits.items():
        images_dst = os.path.join(base_dir, split, "images")
        labels_dst = os.path.join(base_dir, split, "labels")
        os.makedirs(images_dst, exist_ok=True)
        os.makedirs(labels_dst, exist_ok=True)
        count = 0
        while count < qtd and idx < len(imagens):
            img_path = imagens[idx]
            img_name = os.path.basename(img_path)
            label_path = img_path.replace("/images/", "/labels/").replace("\\images\\", "\\labels\\").replace(".jpg", ".txt")
            # Só copia se ainda não existe no destino
            if not os.path.exists(os.path.join(images_dst, img_name)):
                shutil.copy2(img_path, os.path.join(images_dst, img_name))
                if os.path.exists(label_path):
                    shutil.copy2(label_path, os.path.join(labels_dst, os.path.basename(label_path)))
                count += 1
            idx += 1

if __name__ == "__main__":
    # Limpa pastas gerais
    for split in splits:
        limpa_pasta(os.path.join(base_dir, split, "images"))
        limpa_pasta(os.path.join(base_dir, split, "labels"))
    # Copia amostras exclusivas e balanceadas
    for classe_dir, classe_idx in classes:
        copia_amostras_exclusivas(classe_dir, classe_idx)
    print("Redistribuição balanceada e exclusiva concluída.")
