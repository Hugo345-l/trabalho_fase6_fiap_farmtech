import os
import shutil
import random

base_dir = "projeto_visao_computacional/dataset"
splits_proporcao = {"train": 0.8, "val": 0.1, "test": 0.1}  # Proporções padrão
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
    
    # Retorna True se encontrou pelo menos uma anotação da classe especificada
    return count_classe > 0

def distribui_dataset_proporcional():
    """Distribui os arquivos garantindo o balanceamento correto de forma proporcional."""
    
    print("Iniciando balanceamento proporcional do dataset...")
    
    # Limpa as pastas de destino
    for split in splits_proporcao.keys():
        limpa_pasta(os.path.join(base_dir, split, "images"))
        limpa_pasta(os.path.join(base_dir, split, "labels"))
    
    # Determina o número máximo comum de arquivos para ambas as classes
    arquivos_por_classe = {}
    
    for classe_dir, classe_id in classes.items():
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
        
        arquivos_por_classe[classe_id] = list(arquivos_validos.items())
        print(f"Classe {classe_id}: {len(arquivos_por_classe[classe_id])} arquivos válidos")
    
    # Determina o número mínimo de arquivos disponíveis entre as classes
    min_arquivos = min(len(arquivos_por_classe[0]), len(arquivos_por_classe[1]))
    
    print(f"Usando {min_arquivos} arquivos para cada classe (limitado pela menor classe)")
    
    # Calcula quantos arquivos distribuir para cada split, garantindo pelo menos 1 para cada
    arquivos_por_split = {}
    total_restante = min_arquivos
    
    for split, proporcao in list(splits_proporcao.items())[:-1]:  # Todos exceto o último
        qtd = max(1, int(min_arquivos * proporcao))
        if qtd > total_restante:
            qtd = total_restante
        
        arquivos_por_split[split] = qtd
        total_restante -= qtd
    
    # O último split recebe o restante
    ultimo_split = list(splits_proporcao.keys())[-1]
    arquivos_por_split[ultimo_split] = total_restante
    
    # Imprime a distribuição
    print("Distribuição de arquivos por split:")
    for split, qtd in arquivos_por_split.items():
        print(f"  {split}: {qtd} arquivos")
    
    # Agora distribui os arquivos para cada classe
    for classe_id, arquivos in arquivos_por_classe.items():
        random.shuffle(arquivos)  # Embaralha para evitar viés
        
        # Seleciona apenas a quantidade necessária
        arquivos = arquivos[:min_arquivos]
        
        indice = 0
        for split, quantidade in arquivos_por_split.items():
            print(f"Copiando {quantidade} arquivos da classe {classe_id} para {split}")
            
            destino_images = os.path.join(base_dir, split, "images")
            destino_labels = os.path.join(base_dir, split, "labels")
            
            for i in range(quantidade):
                if indice >= len(arquivos):
                    print(f"  AVISO: Índice fora dos limites para a classe {classe_id}")
                    break
                    
                nome_arquivo, (img_path, label_path) = arquivos[indice]
                
                # Copia os arquivos
                shutil.copy2(img_path, os.path.join(destino_images, nome_arquivo))
                shutil.copy2(label_path, os.path.join(destino_labels, os.path.basename(label_path)))
                
                indice += 1
    
    print("Balanceamento proporcional do dataset concluído.")
    
    # Conta o resultado final
    for split in splits_proporcao.keys():
        images_dir = os.path.join(base_dir, split, "images")
        if os.path.exists(images_dir):
            count = len(os.listdir(images_dir))
            print(f"{split.upper()}: {count} imagens no total")

if __name__ == "__main__":
    distribui_dataset_proporcional()
