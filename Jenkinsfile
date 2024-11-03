pipeline {
    agent any  // This will run the pipeline on any available agent

    stages {
        stage('Build') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run unit tests using pytest
                    sh 'pytest'
                }
            }
        }
    }

    post {
        always {
            // Cleanup actions, e.g., archive test results
            junit '**/test-results.xml'  // Optional: Archive test results if using JUnit XML format
        }
    }
}
