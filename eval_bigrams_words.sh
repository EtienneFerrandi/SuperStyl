#! bin/bash

#CONSTITUTION DES CARACTÉRISTIQUES DU TRAIN ET DU TEST

python main.py -s train/* -t words -n 2 -x txt

#constitution du tableau relatif au corpus d'entraînement
python main.py -s train/* -t words -n 2 -f feature_list_words2grams5000mf.json -x txt
mv feats_tests_n2_k_5000.csv train.csv

#constitution du tableau relatif au corpus de test
python main.py -s test/* -t words -n 2 -f feature_list_words2grams5000mf.json -x txt
mv feats_tests_n2_k_5000.csv test.csv


#ÉVALUATION DU MODÈLE EN VALIDATION CROISÉE LEAVE-ONE-OUT

python train_svm.py train.csv --norms --cross_validate leave-one-out