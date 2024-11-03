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
        stage('Deploy') {
            when {
                // Only deploy if the previous stages were successful
                allOf {
                    expression { currentBuild.result == null }
                }
            }
            steps {
                script {
                    // Example deployment command
                    sh '''
                    echo "Deploying application to staging environment..."
                    # Add your deployment commands here
                    # e.g., scp to a server, docker run, etc.
                    '''
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
