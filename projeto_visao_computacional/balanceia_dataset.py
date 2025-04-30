import os
import shutil
import random

base_dir = "projeto_visao_computacional/dataset"
splits = {"train": 40, "val": 5, "test": 5}
classes = {
    "objeto_a_copo": 0,
    "objeto_b_headphones": 1
}

def limpa_pasta(pasta):
    """Limpa o conteúdo de uma pasta se ela existir."""
    if os.path.exists(pasta):
        for arquivo in os.listdir(pasta):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                os.remove(caminho)
            elif os.path.isdir(caminho):
                shutil.rmtree(caminho)
    os.makedirs(pasta, exist_ok=True)

def verifica_classe_arquivo(label_path, classe_id):
    """Verifica se o arquivo contém apenas a classe especificada."""
    if not os.path.exists(label_path):
        return False
    
    with open(label_path, "r") as f:
        linhas = f.readlines()
    
    # Verifica se todas as linhas pertencem à classe especificada
    # e conta quantas anotações há dessa classe
    count_classe = 0
    for linha in linhas:
        if linha.strip():
            try:
                classe = int(linha.strip().split()[0])
                if classe == classe_id:
                    count_classe += 1
                else:
                    # Se encontrar outra classe, não é um arquivo puro
                    return False
            except (ValueError, IndexError):
                # Se falhar na conversão, ignore a linha
                continue
    
    # Retorna True se encontrou exatamente uma anotação da classe especificada
    return count_classe == 1

def distribui_dataset():
    """Distribui os arquivos garantindo o balanceamento correto."""
    
    print("Iniciando balanceamento do dataset...")
    
    # Limpa as pastas de destino
    for split in splits:
        limpa_pasta(os.path.join(base_dir, split, "images"))
        limpa_pasta(os.path.join(base_dir, split, "labels"))
    
    # Processa cada classe
    for classe_dir, classe_id in classes.items():
        print(f"Processando classe: {classe_dir} (ID: {classe_id})")
        
        # Encontra todos os arquivos disponíveis para a classe
        arquivos_validos = {}
        
        for split_origem in ["train", "valid", "test"]:
            images_dir = os.path.join(base_dir, classe_dir, split_origem, "images")
            labels_dir = os.path.join(base_dir, classe_dir, split_origem, "labels")
            
            if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
                continue
                
            for img_name in os.listdir(images_dir):
                if not img_name.endswith(".jpg"):
                    continue
                    
                img_path = os.path.join(images_dir, img_name)
                label_name = os.path.splitext(img_name)[0] + ".txt"
                label_path = os.path.join(labels_dir, label_name)
                
                # Verifica se é um arquivo válido e contém apenas a classe desejada
                if os.path.exists(label_path) and verifica_classe_arquivo(label_path, classe_id):
                    arquivos_validos[img_name] = (img_path, label_path)
        
        print(f"  Encontrados {len(arquivos_validos)} arquivos válidos para a classe {classe_id}")
        
        # Embaralha os arquivos disponíveis
        arquivos_lista = list(arquivos_validos.items())
        random.shuffle(arquivos_lista)
        
        # Distribui para cada split
        indice = 0
        for split, quantidade in splits.items():
            print(f"  Copiando {quantidade} arquivos para {split}")
            
            destino_images = os.path.join(base_dir, split, "images")
            destino_labels = os.path.join(base_dir, split, "labels")
            
            # Copia a quantidade exata de arquivos para o split
            for i in range(quantidade):
                if indice >= len(arquivos_lista):
                    print(f"  AVISO: Não há arquivos suficientes para a classe {classe_id} no split {split}")
                    break
                    
                nome_arquivo, (img_path, label_path) = arquivos_lista[indice]
                
                # Copia os arquivos
                shutil.copy2(img_path, os.path.join(destino_images, nome_arquivo))
                shutil.copy2(label_path, os.path.join(destino_labels, os.path.basename(label_path)))
                
                indice += 1
    
    print("Balanceamento do dataset concluído.")

if __name__ == "__main__":
    distribui_dataset()
