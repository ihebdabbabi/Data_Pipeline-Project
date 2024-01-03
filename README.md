
# Projet_Pipeline_de_donnée

## Introduction
Notre projet pour le module Data Pipeline se concentre sur une étude approfondie des données politiques en prévision des élections présidentielles de 2022. 


Le travail est divisé en trois parties:

* Collecte des données.
* Préparation et Traitement des données ( nettoyage , Suppression ..).
* Orchestration et automatisation du pipeline .

## Les Technologies utilisés
* apache Kafka
* apache Spark
* apache Nifi
* apache nifi-registry
* apache Airflow


## La Collecte des données


Cette première étape est essentielle pour fournir au pipeline de données les informations nécessaires. Vous trouverez ci-dessous l'illustration du schéma créé avec NiFi.

<img width="811" alt="nifi f" src="https://github.com/ihebdabbabi/Data_Pipeline-Project/assets/136711502/c21630d0-75ef-4d2f-a2d4-4b71b2869598">

<img width="907" alt="nifi2" src="https://github.com/ihebdabbabi/Data_Pipeline-Project/assets/136711502/27c8bd28-a792-40a2-9efc-0cff30fddc76">

Notre processus de gestion des données s'articule autour de deux flux distincts, chacun comportant des étapes spécifiques pour assurer la qualité et l'intégrité des informations.

Le premier flux débute avec le composant "GetFile", récupérant les fichiers initiaux, suivis du processus "ConvertRecordToCSVFile" pour la conversion des éléments au format CSV. Ensuite, le composant "EvaluateJsonPath" est utilisé pour évaluer les chemins JSON, et l'étape "UpdateAttribute" permet d'apporter des modifications nécessaires avant de publier les données vers le système Kafka via le composant "PublishKafka".

Parallèlement, le deuxième flux commence avec un nouveau "GetFile" pour récupérer les fichiers initiaux, qui sont ensuite validés avec le composant "ValidateCSV". Les fichiers validés sont fusionnés à l'aide du processus "MergeContent", simplifiant ainsi leur gestion en raison de leur taille minimale. Le fichier fusionné est renommé en "MergedData.csv" via le composant "UpdateAttribute", suivi d'une étape de téléchargement grâce au composant "PutFile". Cette approche structurée garantit une manipulation efficace des données tout au long du processus, facilitant ainsi une utilisation ultérieure dans des environnements comme Spark.

ci dessous une image sur le bucket realisé sur nifi_registry
![nifi_registry](https://github.com/ihebdabbabi/Data_Pipeline-Project/assets/136711502/914fc726-0198-4d83-b047-2067d74d008c)





## Traitement des données

Une fois les données collectées, nous avons effectués plusieurs opérations principalement Pyspark sur les données collectés tel que:

* Suppression des doublons.
* changement des valeurs.
* Traitement des dates.
* Ajout de colonnes .
* visualisation des données.
* Realisation des plots d'analyse de données comme ci dessous.

![Nb_vote_par_dprt](https://github.com/ihebdabbabi/Data_Pipeline-Project/assets/136711502/8878ac80-5404-45a0-bb3c-010e5ab6d0de)
![nbr_moy_vote_par_condidat](https://github.com/ihebdabbabi/Data_Pipeline-Project/assets/136711502/b3784569-b9ed-4687-9bf1-38713b7ff520)


![nb_vote_par_condidat_genre](https://github.com/ihebdabbabi/Data_Pipeline-Project/assets/136711502/b853c445-f252-4732-b371-f5a96a84b14e)


## Orchestration et automatisation du pipeline de données .

Dans le but d'orchestrer et d'automatiser notre flut de données, nous avons un DAG sur Airflow:

Chaque jour, le DAG sur Airflow s'active pour orchestrer les étapes cruciales visant à acquérir et traiter les données spécifiques à chaque candidat..




