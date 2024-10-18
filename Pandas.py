"""
Écrivez un programme Pandas pour créer et afficher un DataFrame à partir des données
de dictionnaire suivantes avec des étiquettes d'index.

 _exam_data = {'name' : ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score' : [12,5, 9, 16,5, np.nan, 9, 20, 14,5, np.nan, 8, 19],

'tentatives' : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualifier' : ['oui', 'non', 'oui', 'non', 'non', 'oui', 'oui', 'non', 'non', 'oui']}

étiquettes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']



"""

import pandas as pd
import numpy as np


exam_data = {
    'NAME': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'SCORE': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'TENTATIVES': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'QUALIFIER': ['oui', 'non', 'oui', 'non', 'non', 'oui', 'oui', 'non', 'non', 'oui'],
    'ETIQUETTE': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
}

exam_data1 = pd.DataFrame(exam_data)

print("\n1-  Imprimons les trois premières lignes à l'aide de la méthode head().")
print(exam_data1.head(3))
print("\n2-  Supprimons les lignes contenant des valeurs NaN.")
print(exam_data1.drop(labels=[3,7]))
print("\n3-  Extrayez les colonnes 'name' et 'score' du DataFrame.")
Name_Score = ['NAME', 'SCORE']
print(exam_data1[Name_Score])

print("\n4-  Écrivez un programme Pandas pour ajouter une nouvelle ligne 'k' ")
k = {
    'NAME': 'Suresh',
    'SCORE': 15.5,
    'TENTATIVES': 1,
    'QUALIFIER': 'oui'
}
exam_data1 = exam_data1._append(k, ignore_index=True)
print(exam_data1)

print("\n5-  Écrivez un programme Pandas pour supprimer la colonne 'attempts'.")
supprimer_colonne = exam_data1.pop('TENTATIVES')
print(exam_data1)

print("\n6-  Ajoutez une nouvelle colonne 'Succès' : si le score est supérieur à 10, nous aurons 1, sinon 0.")



print("\n7-  Après avoir exécuté le DataFrame final, exportez-le dans un fichier CSV nommé 'my_data'.")
exam_data1.to_csv('my_data.csv')
