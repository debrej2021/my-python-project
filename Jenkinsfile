pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run pytest and generate JUnit report
                    sh 'pytest --junitxml=results.xml'
                }
            }
        }
    }

    post {
        always {
            junit 'results.xml'  // This will point to the generated report file
        }
    }
}
