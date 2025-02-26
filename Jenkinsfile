pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/Mohaa922/tpjenkins.git'  // Remplace par l'URL de ton dépôt GitHub
        BRANCH = 'main'  // Remplace par la branche que tu veux utiliser
    }

    stages {
        // Étape 1 : Cloner le dépôt Git
        stage('Cloner le code') {
            steps {
                script {
                    echo "Clonage du dépôt Git..."
                    sh 'rm -rf tpjenkins'  // Supprimer le répertoire existant si nécessaire
                    sh 'git clone --branch ${BRANCH} ${GIT_REPO}'  // Cloner le dépôt
                }
            }
        }

        // Étape 2 : Installer les dépendances
        stage('Installation des dépendances') {
            steps {
                script {
                    echo "Installation des dépendances..."
                    dir('tpjenkins') {  // Naviguer dans le répertoire cloné
                        sh 'pip install -r requirements.txt'  // Installer les dépendances
                    }
                }
            }
        }

        // Étape 3 : Exécuter les tests
        stage('Test') {
            steps {
                script {
                    echo "Exécution des tests unitaires..."
                    dir('tpjenkins') {  // Naviguer dans le répertoire cloné
                        sh 'python -m pytest test_calculator.py'  // Exécuter les tests
                    }
                }
            }
        }

        // Étape 4 : Construire l'image Docker
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Vérification de la connexion à Docker..."
                    sh 'docker --version'  // Vérifier que Docker est installé
                    sh 'docker ps'  // Vérifier que le démon Docker est en cours d'exécution

                    echo "Construction de l'image Docker..."
                    dir('tpjenkins') {  // Naviguer dans le répertoire cloné
                        sh 'docker build -t circle-perimeter .'  // Construire l'image Docker
                    }
                }
            }
        }
    }

    // Déclencheur SCM pour vérifier les changements toutes les 5 minutes
    triggers {
        pollSCM('H/5 * * * *')
    }

    // Actions post-build
    post {
        success {
            echo "Pipeline réussie !"
        }
        failure {
            echo "Pipeline échouée !"
        }
    }
}
