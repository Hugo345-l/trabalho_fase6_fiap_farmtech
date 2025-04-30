import os
import shutil
import glob

base_dir = "projeto_visao_computacional/dataset"
splits = ["train", "val", "test"]
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

def corrige_dataset():
    """Reorganiza corretamente o dataset garantindo a distribuição adequada."""
    
    print("Iniciando correção do dataset...")
    
    # Primeiro, limpa todas as pastas gerais
    for split in splits + ["valid"]:  # Inclui "valid" para limpá-la também
        limpa_pasta(os.path.join(base_dir, split, "images"))
        limpa_pasta(os.path.join(base_dir, split, "labels"))
    
    # Copia arquivos de cada classe para as pastas gerais
    for classe_dir, classe_id in classes.items():
        print(f"Processando classe: {classe_dir} (ID: {classe_id})")
        
        for split in splits:
            # Determina o nome da pasta de origem (mapeia "val" para "valid" nas pastas de origem)
            origem_split = "valid" if split == "val" else split
            
            origem_images = os.path.join(base_dir, classe_dir, origem_split, "images")
            origem_labels = os.path.join(base_dir, classe_dir, origem_split, "labels")
            
            destino_images = os.path.join(base_dir, split, "images")
            destino_labels = os.path.join(base_dir, split, "labels")
            
            # Verifica se as pastas de origem existem
            if not os.path.exists(origem_images) or not os.path.exists(origem_labels):
                print(f"Pasta não encontrada: {origem_images} ou {origem_labels}")
                continue
                
            # Conta arquivos para debug
            imagens = glob.glob(os.path.join(origem_images, "*.jpg"))
            labels = glob.glob(os.path.join(origem_labels, "*.txt"))
            print(f"  {split.upper()}: Encontrado {len(imagens)} imagens e {len(labels)} labels")
            
            # Copia arquivos
            for img_path in imagens:
                img_name = os.path.basename(img_path)
                label_name = os.path.splitext(img_name)[0] + ".txt"
                label_path = os.path.join(origem_labels, label_name)
                
                if os.path.exists(label_path):
                    shutil.copy2(img_path, os.path.join(destino_images, img_name))
                    shutil.copy2(label_path, os.path.join(destino_labels, label_name))
                else:
                    print(f"  AVISO: Label não encontrado para {img_name}")
    
    print("Correção do dataset concluída.")
    
    # Faz uma contagem final para verificar
    for split in splits:
        images_dir = os.path.join(base_dir, split, "images")
        labels_dir = os.path.join(base_dir, split, "labels")
        
        if os.path.exists(images_dir) and os.path.exists(labels_dir):
            img_count = len(os.listdir(images_dir))
            label_count = len(os.listdir(labels_dir))
            print(f"{split.upper()}: {img_count} imagens, {label_count} labels")

if __name__ == "__main__":
    corrige_dataset()
