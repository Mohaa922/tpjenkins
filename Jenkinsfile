pipeline {
    agent any
environment {
        GIT_REPO = 'https://github.com/Mohaa922/tpjenkins.git'  // Remplace par l'URL de ton dépôt GitHub
        BRANCH = 'main'  // Remplace par la branche que tu veux utiliser
    }
 
    stages {
        stage('Cloner le code') {
            steps {
                script {
                    // Supprimer le répertoire existant si nécessaire
                    sh 'rm -rf tpjenkins'
                    // Cloner le dépôt depuis GitHub sans utiliser SCM Jenkins
                    sh 'git clone --branch ${BRANCH} ${GIT_REPO}'
                }
            }
        }
 
        stage('Installation des dépendances') {
            steps {
                script {
                    // Naviguer dans le répertoire du code cloné et installer les dépendances
                    dir('tpjenkins') {
                        sh 'pip install -r requirements.txt'  // Assure-toi d'avoir un fichier requirements.txt
                    }
                }
            }
        }
    stages {
        stage('Test') {
            steps {
                echo "Exécution des tests unitaires..."
                sh 'python -m pytest test_calculator.py'
            }
        }
    }

    triggers {
        pollSCM('H/5 * * * *') // Vérifie les changements toutes les 5 minutes
    }

    post {
        success {
            echo "Pipeline réussie !"
        }
        failure {
            echo "Pipeline échouée !"
        }
    }
}
