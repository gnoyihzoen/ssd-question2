pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git url: 'https://your-repo-url.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r webapp/requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python3 webapp/test_webapp.py'
            }
        }

        stage('UI Test') {
            steps {
                sh 'curl -s --fail http://web/ || exit 1'
            }
        }
    }
}
