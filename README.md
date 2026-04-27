Atelier proposé aux étudiant d'Unilasalle en décembre 2025 portant sur la prise en mains de méthodes d'interpolations/réduction de dimensions 2D et Machine Learning (U-net et AE). 

Ce notebook présente un **atelier pratique sur la réduction de dimensionnalité** appliquée aux données océaniques. L'objectif principal est de développer des stratégies pour **compresser les données de température de surface (SST)** tout en préservant la meilleure qualité de reconstruction possible.

Les données de trvaail sont issues des produit MERCATOR Océan (Glorys12) plus précismsent sur la variable SST (Atlantique Sud à 1/12° de résolution, format .nc). 
Le script Glorydata.py permet de récupérer le dataset complet utilisé dans l'atelier depuis L'API MLERCATOR. 

## Processus de résolution proposé : 
* Installations et Configuration de l'environnement python (conda)
* Exploration des données Glorys12
* **A. Analyse en Composantes Principales (ACP / PCA)**
* **B. Auto-Encodeur (AE)**
* **C. U-Net**
* Préparation des données (DataLoader, train/test; normalization)
* Implémentation Lightning
* Résultats du comparatif avec visualisation dynaique (ipwidgets)
  
## Notion abordées sur les bibliothèques suivantes : 

- **PyTorch** : Framework deep learning
- **PyTorch Lightning** : Abstraction haut niveau (structure, training loops, callbacks)
- **scikit-learn** : PCA et preprocessing
- **xarray** : Manipulation de données géophysiques (NetCDF)
- **Cartopy** : Cartographie et visualisations géographiques
- **Matplotlib** : Plots statiques
- **ipywidgets** : Interfaces interactives Jupyter

Recommandation Hardware et générales :
- **Batch size** : 8 échantillons
- **Epochs** : 20-50 selon le modèle
- **Hardware** : GPU recommandé (accélérateur CUDA disponible)

L'ensemble des données et du NB sont disponibles égalementt sur Google colab : https://drive.google.com/drive/folders/1YIku0SvPegErw0oIhWcCDqJOnC60KPd8?usp=drive_link si vous souhaiter le faire tourner sur l'infra GOOGLE. 
