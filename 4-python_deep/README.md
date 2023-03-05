# Apprentissage profond pour le traitement du langage naturel

Dans les Travaux Pratiques (TPs) précédents, vous avez appris les bases de la programmation Python, comment traiter un ensemble de données textuelles, comment extraire des caractéristiques telles que TF-IDF et comment entraîner différents modèles d'apprentissage automatique, notamment les SVM et les MLP (réseaux neuronaux feed-forward), à l'aide du package `sklearn`. Toutefois, le package `sklearn` ne permet pas de concevoir et de former des réseaux neuronaux personnalisés de manière plus détaillée. Par conséquent, vous apprendrez ici à utiliser `PyTorch` pour définir, former et évaluer votre propre modèle de réseau de neurones pour différentes tâches. Vous apprendrez également les bases de l'apprentissage profond et comment utiliser des représentations profondes pré-entraînées des données, telles que les modèles BERT, au lieu des fonctions TF-IDF traditionnelles. Vous trouverez ci-dessous une liste de ce que vous apprendrez au cours de ce travail pratique.

## Installation

Ici, comme dans le TP précédent, nous travaillons avec `JupyterLab`. Si vous avez déjà installé l'environnement nécessaire, vous pouvez simplement le charger par executant `conda activate TP_NLP_2023` et ensuite `jupyter-lab`, sinon vous pouvez suivre les instructions ci-dessous :

Pour installer l'environnement nécessaire aux TPs, après avoir installé la dernière version de [Miniconda3](https://docs.conda.io/en/latest/miniconda.html) (ou Anaconda3, si vous souhaitez une interface graphique), exécutez les commandes suivantes :

````bash
conda create -n "TP_NLP_2023" python=3.8 # creates the environment
conda activate TP_NLP_2023  # activates the environment
conda install -c conda-forge jupyterlab=3.6.1  # installs jupyterlab on the environment
jupyter-lab # to launch jupet-lab!
````
Notez que le travail sur ce TP peut également être réalisé par différents moyens, notamment en utilisant un éditeur de texte (comme [Visual Studio Code](https://code.visualstudio.com/)), ou [google colab](https://colab.research.google.com/). 

Ensuite, cliquez sur `TP.ipynb` pour lancer le TP.

## À rendre

Après avoir répondu aux questions dans ` TP.ipynb`, renommer le fichier comme `TP_4_[name].ipynb` avec votre nom au lieu de `[name]`, et envoyez le fichier à [Chamilo](https://chamilo.univ-grenoble-alpes.fr/).
