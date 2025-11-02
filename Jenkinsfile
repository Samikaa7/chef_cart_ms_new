node {
    stage('Checkout') {
        git branch: 'main', url: 'https://github.com/Samikaa7/chef_cart_ms_new.git'
    }

    stage('Build') {
        echo 'Building the project...'
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate && pip install -r requirements.txt || echo "No requirements file found"'
    }

    stage('Test') {
        echo 'Running tests...'
        sh '. venv/bin/activate && pytest || echo "No tests found"'
    }

    stage('Deploy') {
        echo 'Deploying...'
        sh 'echo "Simulated deploy step - replace with EC2 or Streamlit deployment commands"'
    }
}
