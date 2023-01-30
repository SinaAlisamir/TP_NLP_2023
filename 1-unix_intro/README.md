# Introduction au traitement de texte par l'utilisation de commandes unix
Le lecteur est ici présenté aux bases d'Unix et aux commandes de terminal qu'il est utile de connaître pour manipuler de texte. Ces travaux pratiques utilisent beaucoup de matériel provenant [des travaux pratiques de l'année précédente (2022) sur ce sujet](https://github.com/lorelupo/tp_nlp/tree/main/tp_intro). Le plan de ce travail pratique est le suivant:

1. Aperçu: Ce que vous allez apprendre ici
2. Outils: La boîte à outils dont vous aurez besoin ici (et très probablement après ce cours)
3. Redirection des entrées/sorties: Comment passer les entrées et sorties avec les commandes du terminal
4. Exercices: Les exercices qui seront pratiqués ici
5. À rendre: Comment envoyer les résultats des exercices pour les faire évaluer

## 1- Aperçu

Voici ce que vous allez apprendre ici :

- Des encodages des characters de text et les manipuler
- Compter les mots dans un texte
- Ordonner une liste de mots par ordre alphabétique ou ordre numérique
- Calculer des statistiques d’occurrences et de co-occurrences
- Extraire une information utile d'un dictionnaire
- Extraire une information utile d'un texte
- Transformer un texte

## 2- Outils

- `cat/head/tail` : afficher (la totalité/le début/la fin) d'un fichier à l'écran
- `less` : afficher un fichier avec défilement
- `grep` : chercher un motif (expression régulière)
- `sort` : trier les lignes
- `uniq -c` : éliminer ou compter les doublons
- `tr` : transposer ou éliminer des caractères
- `wc` : compter les lignes, mots et caractères
- `sed` : éditer (remplacer, éliminer) une chaîne avec des expressions régulières
- `awk` : langage d'examen et de traitement de motifs
- `cut` : extraire des colonnes
- `paste` : "coller" des lignes des differents fichiers
- `join` : équivalent au JOIN de SQL
- `xxd` : binaire vers hex ou l'envers
- `rev`: inverser l'ordre des lignes
- `wget`: telecharger une fichier d'internet vers l'ordinateur local
- Conversion d'encodages de caractères : `iconv`

**Suggestions** :

- Pensez toujours à lire la page `man` d'un outil en cas de doute sur les paramètres et fonctionnalités de l'outil. Par exemple, la commande `man wc` indique de quelle façon on peut compter seulement les lignes (`-l`) ou seulement les mots (`-w`) dans un fichier.
- Beaucoup d’exercices nécessitent l'utilisation d'expressions régulières ("regex"), i.e. un "langage" permettant des règles sophistiquées de recherche et de remplacement de motif. Vous pouvez tester vos regex ici: https://regex101.com/.

3- Redirection des entrées/sorties
--------------------------------

Par défaut, la plupart des outils lit les entrées (stdin) à partir du clavier et écrit les sorties (stdout) à l'écran. On peut rediriger les entrées et les sorties vers des fichiers, à l'aide des commandes suivantes :

`<` &nbsp; Lire depuis un fichier d'entrée
`>` &nbsp; Écrire dans un fichier de sortie
`|` &nbsp; Rediriger la sortie de la commande précédente vers l'entrée de la commande suivante (pipe)

4- Exercices
---------

**Données utilisé pour les exercices** : [RADIOS.txt](https://raw.githubusercontent.com/lorelupo/tp_nlp/main/tp_intro/RADIOS.txt). Ce fichier contient des transcriptions d'enregistrements radiophoniques comme France inter et RFI. Vous pouvez obtenir le texte avec la commande suivante :

```bash
wget https://raw.githubusercontent.com/lorelupo/tp_nlp/main/tp_intro/RADIOS.txt
```


---------
- **Exercice 0** : Des encodages des characters de text

- L'encodage des caractères est le processus qui consiste à attribuer des numéros aux caractères graphiques, en particulier les caractères écrits du langage humain, afin de permettre leur stockage, leur transmission et leur transformation à l'aide d'ordinateurs numériques [Voir ici pour plus d'info](https://en.wikipedia.org/wiki/Character_encoding). Voici quelque exemple des plus connus encodages: [US-ASCII](https://en.wikipedia.org/wiki/US-ASCII), [UTF-8](https://en.wikipedia.org/wiki/UTF-8), [UTF-16](https://en.wikipedia.org/wiki/UTF-16), [UTF-32](https://en.wikipedia.org/wiki/UTF-32)

- Des caractères différents pour des langues différentes doivent être supportés par l'encodage, afin d'être écrits ou lus. Par exemple, l'ASCII a été conçu pour prendre en charge la langue anglaise, et ne possède donc pas les caractères accentués, nécessaires pour coder tous les caractères utilisés dans d'autres langues latins, comme le français.

- La commande `iconv` peut être utilisée pour convertir un texte en différents encodages. Vous pouvez utiliser la page `man` de `iconv` pour plus d'informations.

- **Q0**: Remplacer tous les caractères français accentués dans le fichier `RADIOS.txt` en utilisant la commande `iconv`. Et puis, enregistrez le nouveux text sans accents, comme `[name]_TP1_E0_Q0.txt`

  - **Aide**: Vous pouvez utiliser `//TRANSLIT` avec la commande `iconv` pour convertir, par exemple `ascii//TRANSLIT` signifie: utiliser `ascii` mais si c'est pas possibles pour certains caractères, remplacer-les.

- **Réponse**:

  ```bash
  
  ```

---------
- **Exercice 1** : Trouver une commande qui transforme tout le texte en lettres majuscules

  - **Q0**: Rendre tout le texte en lettres majuscules et enregistrez les 200 premiere lignes dans `[name]_TP1_E1_Q0.txt`
    - **Entrée** : Fichier texte RADIOS.txt
    - **Aide**: Pensez à bien gérer les accents
  - **Réponse**:

  ```bash
  
  ```

---------

- **Exercice 2** : Trouver la suite d'instructions qui permet de compter les mots dans un texte

  - **Pour commencer**: Liste des mots avec leur nombre d'apparitions dans le texte (enregestrez la sortie comme `RADIOS.hist`)

  - **Aide** : utiliser `tr`, `sort` et `uniq`, `penser` à "piper" (`|`) les instruction

  - **Q0** : Quel est le mot qui apparaît exactement 1732 fois dans ce texte ? (Enregistrez le chifre et le mot separer par espace dans `[name]_TP1_E2_Q0.txt`)

  - **Réponse**:

    ```bash
    
    ```
    
  - **Q1** : Combien de fois le mot "orange" apparaît dans ce texte ? 
  
  - Enregistrez le chifre et le mot separer par espace, comme `[name]_TP1_E2_Q1.txt`
  
- **Réponse**:
  
  ```bash
    
    ```
  
- **Aide**: Pour les question suivants pensez bien à regarder la page man de `sort`
  
- **Q2** : Trier les mots de RADIOS.hist par fréquence d'apparition et en igniorant les majuscules/minuscules ? 
  
  - Enregistrez les chifres et les mots separer par espace, comme `[name]_TP1_E2_Q2.txt`
  
- **Réponse**:
  
  ```bash
    
    ```
    
  - **Q3** : Trier les mots de RADIOS.hist par ordre alphabétique ? 
  
  - Enregistrez les chifres et les mots separer par espace, comme `[name]_TP1_E2_Q3.txt`
  
- **Réponse**:
  
  ```bash
    
    ```
  
- **Q4** : Trier les mots de RADIOS.hist par ordre des mots qui rime ensemble ?
  
  - **Exemple**: mettre ensemble tous les mots qui finissent par "-ment". 
    - **Aide**: Utilisez la commande unix `rev` 
    - Enregistrez les chifres et les mots separer par espace comme `[name]_TP1_E2_Q4.txt`)
  
- **Réponse**:
  
  ```bash
    
    ```

---------

- **Exercice 3** : Trouver et compter les n-grammes du texte RADIOS.txt

  - Pour chaque n-gramme, avec n=2,3,4, générer un fichier de statistiques où chaque ligne est de la forme "mot1 mot2 nb" pour les bi-grammes, "mot1 mot2 mot3 nb" pour les tri-grammes, etc.
  
- Pour savoir plus de n-gram dans NLP: [Understanding Word N-grams in NLP](https://towardsdatascience.com/understanding-word-n-grams-and-n-gram-probability-in-natural-language-processing-9d9eef0fa058)
  
- **Attention**: Par mot ici, nous entendons chaque ensemble de caractères séparés par un espace.
  
- **Q0** : Enregistrez tous les lignes avec le 2-gramme "il est" dans le texte ?
  
    - Enregistrez le stdout comme `[name]_TP1_E3_Q0.txt`
    
  - **Réponse**:
  
  ```bash
  
  ```
  
  - **Q1** : Enregistrez combien de fois le 2-gramme "il est" apparaît dans ce texte ?
  
  - Enregistrez le stdout comme `[name]_TP1_E3_Q1.txt`
  
- **Réponse**:
  
  ```bash
  
  ```
  
  - **Aide**: Pensez à utiliser les commandes tail et paste pour les questions suivants. Par example, `tail +3` peut être utilisé pour imprimer toutes les lignes sauf les deux premières.
  
  - **Q2** : Combien de 3-grammes distincts sont trouvés dans ce texte ?
  
    - Enregistrez le stdout comme `[name]_TP1_E3_Q2.txt`
  
  - **Réponse**:
  
    ```bash
    
    ```
    
  - **Q3** : Quel est le 3-gramme le plus fréquent ?
  
    - Afficher la frequance et apres le 3-gramme, example: "45 dans le monde".
    - Enregistrez le stdout comme `[name]_TP1_E3_Q3.txt`
  
  - **Réponse**:
  
    ```bash
    
    ```
  

---------

- **Exercice 4** : Filtrer les lignes avec `grep`
- Pensez à regarder la page `man` de `grep` pour cet exercise. 
- Les examples utiles:
  
| Commande                                            | Description                                  |
| --------------------------------------------------- | -------------------------------------------- |
| `grep '[A-Z]'`                                      | filtre lignes contenant une majuscule        |
| `grep '^[A-Z]'`                                     | filtre lignes commençant par une majuscule   |
| `grep '[A-Z]$'`                                     | filtre lignes finissant par une majuscule    |
| `grep '^[A-Z]*$'`                                   | filtre lignes entièrement majuscules         |
| `grep '[aeiouAEIOU]'`                               | filtre lignes contenant une voyelle          |
| `grep '^[aeiouAEIOU]'`                              | filtre lignes commençant par une voyelle     |
| `grep '[aeiouAEIOU]$'`                              | filtre lignes finissant par une voyelle      |
| `grep '^[^aeiouAEIOU]'`                             | filtre lignes commençant par une non-voyelle |
| `grep '[^aeiouAEIOU]$'`                             | filtre lignes finissant par une non-voyelle  |
| `grep '[aeiouAEIOU].*[aeiouAEIOU]'`                 | filtre lignes avec au moins deux voyelles    |
| `grep '^[^aeiouAEIOU]*[aeiouAEIOU][^aeiouAEIOU]*$'` | filtre lignes avec exactement une voyelle    |

  - Les expressions régulières:

| Expression      | Match                                    |
| --------------- | ---------------------------------------- |
| `a`             | la lettre "a"                            |
| `[a-z]`         | une lettre minuscule                     |
| `[A-Z]`         | une lettre majuscule                     |
| `[0-9]`         | un chiffre                               |
| `[0123456789]`  | un chiffre                               |
| `[aeiouAEIOU]`  | une voyelle (basé sur anglais)           |
| `[^aeiouAEIOU]` | tout sauf une voyelle (basé sur anglais) |
| `.`             | un caractère                             |
| `^`             | début de ligne                           |
| `$`             | fin de ligne                             |
| `x*`            | "x" répété 0 fois ou plus                |
| ``x+``          | "x" répété 1 fois ou plus                |
| `x\|y`          | "x" ou "y"                               |

  **Attention** : Les outils différents (`grep`, `sed`, etc.) ont différents caractères d'échappement (e.g. `;'"#$&*?[]<>{}\`). Pour utiliser ces caractères dans des regex, il faut placer `\` avant. E.g. `\{` pour utiliser `{`.

  - - Pour savoir plus de n-gram dans NLP: [Understanding Word N-grams in NLP](https://towardsdatascience.com/understanding-word-n-grams-and-n-gram-probability-in-natural-language-processing-9d9eef0fa058)
  
  - **Attention**: Par mot ici, nous entendons chaque ensemble de caractères séparés par un espace.
  
  - **Q0** : Enregistrez tous les mots uniques de 9 lettres, qui existent dans RADIOS.txt 
  
    - Enregistrez le stdout comme `[name]_TP1_E4_Q0.txt`
  
  - **Réponse**:
  
    ```bash
    
    ```
    
  - **Q1** : Enregistrez tous les mots uniques sans voyelle, qui existent dans RADIOS.txt 
  
    - Enregistrez le stdout comme `[name]_TP1_E4_Q1.txt`
    - **Attention**: il faut oublier les voyelles avec accent!
  
  - **Réponse**:
  
    ```bash
    
    ```


---------

- **Exercice 5** : Remplacements de séquences avec `sed`

  - **Utilisation**: L'outil `sed` permet de remplacer du texte à l'aide d'expressions régulières. Par exemple, la commande `sed 's/exp1/exp2/[options]'` va remplacer (s) l'expression  `exp1` par l'expression `exp2` avec les `options` mentionnés. L'option est souvent la lettre `g` pour dire que toutes les occurrences sur une même ligne doivent être remplacées. Par exemple :

    - `sed 's/[éèêë]/e/g'` remplace toutes les lettres "e" accentuées par une lettre non-accentuée
    - `sed 's/\([^ ]*\)ation /\U\1ATION /g'` transforme les mots qui finissent par le suffixe "ation" en majuscules, par exemple, "habitation" devient "HABITATION"

    **Suggestion**: On peut éviter d'échapper les caractères comme `()` avec l'option `-E`. E.g. `sed -E 's/([^ ]*)ation /\U\1ATION /g'` == `sed 's/\([^ ]*\)ation /\U\1ATION /g'`.

  - **Suggestion**: Pensez à regarder la page `man` de `sed` pour plus d'informations.

  - `awk` est également un outil alternatif à `sed`, qui est souvent utilisé pour transformer du text.

  - **Attention aux utilisateurs du Mac**: 

    - `sed` native fonctionne un peu différemment entre `GNU` et `BSD` architectures, pour resoudre ce problème, les utilisateurs du Mac peut installer la version sed pour `GNU`:

      ```bash
      brew install gnu-sed
      alias sed=gsed
      ```

  - **Q0** : Rajouter un point final à chaque ligne de RADIOS.txt et mettre la première lettre de chaque ligne en majuscule.

    - Enregistrez le stdout comme `[name]_TP1_E5_Q0.txt`

  - **Réponse**:

    ```bash
    
    ```

  - **Q1** : Remplacer toute occurrence de deux mots identiques consécutifs dans RADIOS.txt par une seule occurrence de ce mot, par exemple, "de de" devient "de".

    - Enregistrez le stdout comme `[name]_TP1_E5_Q1.txt`

  - **Réponse**:

    ```bash
  
    ```
  

---------

## 5- À rendre

Ici, la sortie de chaque exercice (le stdout) doit être placée dans un fichier texte nommé comme suit :

-  `[name]_TP[TP number]_E[excercise number]_Q[question number].txt` -> Example: AlanLopez_TP1_E2_Q0.txt se réfère à la sortie de TP1, excersie 2, question 0, faite par Alan Lopez.

Puis, veuillez écrire les lignes de commande utilisées dans les sections `Réponse:` de ce fichier.

Compressez ensuite tous vos fichiers texte, ainsi que votre version modifiée de ce fichier avec les réponses, sous forme de zip et envoyez le fichier zip à [Chamilo](https://chamilo.univ-grenoble-alpes.fr/).

Veuillez **faire très attention aux noms des fichiers**, car ils seront traités automatiquement et toute erreur dans le nom peut **faire en sorte** que votre **travail** ne soit **pas crédité**.

 



