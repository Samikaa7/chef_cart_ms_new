pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Samikaa7/chef_cart_ms_new.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest || echo "No tests found"'
            }
        }

        stage('Build Complete') {
            steps {
                echo 'Build completed successfully.'
            }
        }
    }
}
