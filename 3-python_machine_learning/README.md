# Apprentissage automatique pour les signaux acoustiques et les textes

Ce Travail Pratique (TP) fournit une introduction aux bases de l'apprentissage automatique (ML) pour les signaux acoustiques et le texte en utilisant Python. Le ML fait référence à un ensemble d'algorithmes d'intelligence artificielle (IA) qui apprennent à effectuer une tâche à partir de données. Le type de données utilisé est généralement désigné comme la modalité utilisée pour le ML. Ici, nous travaillerons avec de l'audio (spécifiquement des signaux acoustiques) et du texte, et les tâches considérées ici sont la classification de sentiments à partir de texte, la classification d'émotions à partir de signaux acoustiques, et la classification de genre pour les signaux acoustiques. À la fin de ce travail pratique, vous apprendrez à traiter des données textuelles et acoustiques, à extraire des caractéristiques et à former et évaluer des modèles d'apprentissage automatique.

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

Après avoir répondu aux questions dans ` TP.ipynb`, renommer le fichier comme `TP_3_[name].ipynb` avec votre nom au lieu de `[name]`, et envoyez le fichier à [Chamilo](https://chamilo.univ-grenoble-alpes.fr/).

 



