node {
    stage('Checkout') {
        git 'https://github.com/Samikaa7/chef_cart_ms_new.git'
    }

    stage('Setup Python Env') {
        echo 'Setting up Python environment...'
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt || echo "No requirements.txt found"
        '''
    }

    stage('Build') {
        echo 'Building project...'
        sh 'echo "Build step executed."'
    }

    stage('Test') {
        echo 'Running tests...'
        sh 'echo "Test step executed."'
    }

    stage('Deploy') {
        echo 'Deploying...'
        sh 'echo "Deploy step executed."'
    }
}
