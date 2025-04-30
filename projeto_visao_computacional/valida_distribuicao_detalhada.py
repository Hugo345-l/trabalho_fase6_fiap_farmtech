import os

splits = ["train", "val", "test"]
base_dir = "projeto_visao_computacional/dataset"
classes = {0: "Copo", 1: "Fone"}

def analisa_dataset():
    """Analisa detalhadamente o dataset, mostrando imagens e anotações por classe."""
    
    for split in splits:
        print(f"\n=== {split.upper()} ===")
        
        # Diretórios
        images_dir = os.path.join(base_dir, split, "images")
        labels_dir = os.path.join(base_dir, split, "labels")
        
        if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
            print(f"  Pastas não encontradas para {split}")
            continue
            
        # Contagem de imagens
        imagens = len(os.listdir(images_dir))
        labels = len(os.listdir(labels_dir))
        
        print(f"  Total: {imagens} imagens, {labels} arquivos de label")
        
        # Contagem por classe
        imagens_por_classe = {classe_id: 0 for classe_id in classes}
        anotacoes_por_classe = {classe_id: 0 for classe_id in classes}
        imagens_multiplas_anotacoes = 0
        
        for label_file in os.listdir(labels_dir):
            if not label_file.endswith(".txt"):
                continue
            
            # Mapeia classes presentes neste arquivo
            classes_neste_arquivo = set()
            total_anotacoes = 0
            
            with open(os.path.join(labels_dir, label_file), "r") as f:
                for linha in f:
                    if linha.strip():
                        try:
                            classe = int(linha.strip().split()[0])
                            if classe in classes:
                                classes_neste_arquivo.add(classe)
                                anotacoes_por_classe[classe] += 1
                                total_anotacoes += 1
                        except (ValueError, IndexError):
                            continue
            
            # Incrementa contagem de imagens para cada classe presente
            for classe in classes_neste_arquivo:
                imagens_por_classe[classe] += 1
                
            # Verifica se tem múltiplas anotações
            if total_anotacoes > 1:
                imagens_multiplas_anotacoes += 1
        
        # Relatório detalhado
        print("  Contagem de imagens por classe:")
        for classe_id, nome_classe in classes.items():
            print(f"    {nome_classe} ({classe_id}): {imagens_por_classe[classe_id]} imagens")
        
        print("  Contagem de anotações por classe:")
        for classe_id, nome_classe in classes.items():
            print(f"    {nome_classe} ({classe_id}): {anotacoes_por_classe[classe_id]} anotações")
            
        if imagens_multiplas_anotacoes > 0:
            print(f"  Imagens com múltiplas anotações: {imagens_multiplas_anotacoes}")

if __name__ == "__main__":
    analisa_dataset()
