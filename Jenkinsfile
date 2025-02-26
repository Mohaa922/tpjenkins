pipeline {
    agent any

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
