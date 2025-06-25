pipeline {
    agent any

    environment {
        SONARQUBE_SCANNER_HOME = tool 'SonarScanner'  
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonar') { 
                    sh """
                    ${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner \
                      -Dsonar.projectKey=ssd-question2 \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://sonarqube:9000 \
                      -Dsonar.login=admin \
                      -Dsonar.password=your_student_id_here
                    """
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
