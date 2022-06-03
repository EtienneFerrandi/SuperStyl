#! bin/bash

#CONSTITUTION DES CARACTÉRISTIQUES DU TRAIN ET DU TEST

python main.py -s train/* -t words -x txt

#constitution du tableau relatif au corpus d'entraînement
python main.py -s train/* -t words -f feature_list_words1grams5000mf.json -x txt
mv feats_tests_n1_k_5000.csv train.csv

#constitution du tableau relatif au corpus de test
python main.py -s test/* -t words -f feature_list_words1grams5000mf.json -x txt
mv feats_tests_n1_k_5000.csv test.csv


#ÉVALUATION DU MODÈLE EN VALIDATION CROISÉE LEAVE-ONE-OUT

python train_svm.py train.csv --norms --cross_validate leave-one-out