#! bin/bash

#CONSTITUTION DES CARACTÉRISTIQUES DU TRAIN ET DU TEST

#génération de la liste de trigrammes d'affixes de mots
python main.py -s train/* -t chars -n 3 -x txt
python features_filter.py -f feature_list_chars3grams5000mf.json --affixes_grams

#on s'appuie sur la liste des trigrammes d'affixes pour dresser les caractéristiques
#constitution du tableau relatif au corpus d'entraînement
python main.py -s train/* -t chars -n 3 -f feature_list_chars3grams5000mf_affixes.json -x txt
mv feats_tests_n3_k_5000.csv train.csv
#constitution du tableau relatif au corpus de test
python main.py -s test/* -t chars -n 3 -f feature_list_chars3grams5000mf_affixes.json -x txt
mv feats_tests_n3_k_5000.csv test.csv


#ÉVALUATION DU MODÈLE EN VALIDATION CROISÉE LEAVE-ONE-OUT

python train_svm.py train.csv --norms --cross_validate leave-one-out


