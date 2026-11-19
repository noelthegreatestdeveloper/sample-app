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
                sh '''
                    python3 -m venv venv
                    ./venv/bin/python -m pip install --upgrade pip
                    ./venv/bin/python -m pip install flask pytest
                '''
            }
        }

        stage('Automated Tests') {
            steps {
                sh './venv/bin/python -m pytest -v'
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
