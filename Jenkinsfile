node {
    stage('Checkout') {
        git branch: 'main', url: 'https://github.com/Samikaa7/chef_cart_ms_new.git'
    }

    stage('Setup Environment') {
        echo 'Setting up Python environment...'
        sh '''
            #!/bin/bash
            set -e

            echo "Checking Python..."
            if ! command -v python3 &> /dev/null; then
                echo "Python3 not found. Installing..."
                sudo apt-get update -y
                sudo apt-get install -y python3 python3-venv python3-pip
            fi

            python3 --version

            echo "Creating virtual environment..."
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip

            if [ -f requirements.txt ]; then
                echo "Installing dependencies..."
                pip install -r requirements.txt
            else
                echo "⚠️ No requirements.txt found, skipping dependencies."
            fi
        '''
    }

    stage('Run Tests') {
        echo 'Running tests...'
        sh '''
            #!/bin/bash
            set -e
            . venv/bin/activate
            if [ -f test_script.py ]; then
                python3 test_script.py
            else
                echo "⚠️ No test_script.py found. Skipping tests."
            fi
        '''
    }

    stage('Build Complete') {
        echo '✅ Build completed successfully.'
    }
}
