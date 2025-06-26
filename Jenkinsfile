pipeline {
  agent any

  environment {
    SONARQUBE_SCANNER_HOME = tool 'SonarScanner'
    VENV_DIR = 'venv'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python Environment') {
      steps {
        sh '''
          python3 -m venv ${VENV_DIR}
          . ${VENV_DIR}/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Dependency Check') {
      steps {
        sh '''
          . ${VENV_DIR}/bin/activate
          pip check
        '''
      }
    }

    stage('Unit and HTTP Testing') {
      steps {
        sh '''
          . ${VENV_DIR}/bin/activate
          pytest tests/
        '''
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('MySonar') {
          withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
            sh """
            ${SONARQUBE_SCANNER_HOME}/bin/sonar-scanner \
              -Dsonar.projectKey=ssd-question4 \
              -Dsonar.sources=. \
              -Dsonar.exclusions=venv/** \
              -Dsonar.host.url=http://sonarqube:9000 \
              -Dsonar.token=${SONAR_TOKEN}
            """
          }
        }
      }
    }
  }
}
