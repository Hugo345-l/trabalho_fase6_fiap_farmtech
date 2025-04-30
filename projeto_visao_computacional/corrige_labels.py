import os
from glob import glob

# Defina os caminhos das pastas de labels
pastas = [
    {
        "pasta": "projeto_visao_computacional/dataset/objeto_a_copo",
        "classe": "0"
    },
    {
        "pasta": "projeto_visao_computacional/dataset/objeto_b_headphones",
        "classe": "1"
    }
]

def corrige_labels(pasta_base, classe_correta):
    for split in ["train", "valid", "test"]:
        labels_dir = os.path.join(pasta_base, split, "labels")
        if not os.path.isdir(labels_dir):
            continue
        for label_path in glob(os.path.join(labels_dir, "*.txt")):
            linhas_corrigidas = []
            with open(label_path, "r", encoding="utf-8") as f:
                for linha in f:
                    partes = linha.strip().split()
                    if len(partes) > 0:
                        partes[0] = classe_correta
                        linhas_corrigidas.append(" ".join(partes))
            with open(label_path, "w", encoding="utf-8") as f:
                for linha in linhas_corrigidas:
                    f.write(linha + "\n")
            print(f"Corrigido: {label_path}")

if __name__ == "__main__":
    for item in pastas:
        corrige_labels(item["pasta"], item["classe"])
    print("Correção concluída.")
