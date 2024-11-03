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
                    // Debugging: Check if Docker is available
                    sh 'docker --version'
                    sh 'docker info'
                    // Build the Docker image
                    sh '''
                    echo "Building Docker image..."
                    docker build -t my-flask-app .
                    '''
                    // Run the Docker container
                    sh '''
                    echo "Deploying application to staging environment..."
                    docker run -d -p 5000:5000 my-flask-app
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
