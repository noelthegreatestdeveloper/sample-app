
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code downloaded successfully.'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install flask pytest'
            }
        }

        stage('Automated Tests') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Pipeline failed. Please check the errors.'
        }
    }
}
