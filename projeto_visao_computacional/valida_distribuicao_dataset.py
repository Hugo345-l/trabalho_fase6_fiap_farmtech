import os

splits = ["train", "val", "test"]
base_dir = "projeto_visao_computacional/dataset"

def conta_classes(labels_dir):
    contagem = {0: 0, 1: 0}
    for label_file in os.listdir(labels_dir):
        if not label_file.endswith(".txt"):
            continue
        with open(os.path.join(labels_dir, label_file), "r") as f:
            for line in f:
                if line.strip():
                    classe = int(line.strip().split()[0])
                    if classe in contagem:
                        contagem[classe] += 1
    return contagem

if __name__ == "__main__":
    for split in splits:
        labels_dir = os.path.join(base_dir, split, "labels")
        if os.path.exists(labels_dir):
            contagem = conta_classes(labels_dir)
            print(f"{split.upper()}: Copo (0): {contagem[0]}, Fone (1): {contagem[1]}")
        else:
            print(f"{split.upper()}: Pasta não encontrada.")
