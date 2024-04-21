# To-Do List and Technical Shortcuts

Cette liste met en évidence les améliorations prévues et les raccourcis techniques pris en raison de contraintes de temps. 

## Raccourcis techniques utilisés
- **Utilisation de dictionnaires et de `deque` comme solutions temporaires**: Pour éviter les problèmes de complexité lors de la manipulation des données, les dictionnaires et les `deque` ont été utilisés. Cela devrait être remplacé par une solution de base de données appropriée à l'avenir ( une base de données relationnelle ou NoSQL qui supporte les structures complexes comme les tableaux (arrays) ).
- **Utilisation de codage URL pour des caractères spéciaux**: L'utilisation de "%2F" a été adoptée comme solution de contournement pour permettre le passage de l'opérateur division ("/") dans les routes de l'API.
Il faut améliorer la gestion des opérateurs spéciaux et éviter les problèmes liés à l'encodage.
- **Ajout de tests unitaires**
- **Amélioration de la documentation**: La documentation du code est actuellement minimaliste. Il faut améliorer les commentaires, les docstrings, et les guides de développement.