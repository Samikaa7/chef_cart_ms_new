node {
    stage('Checkout') {
        git branch: 'main', url: 'https://github.com/Samikaa7/chef_cart_ms_new.git'
    }

    stage('Setup Environment') {
        echo 'Setting up Python environment...'
        sh '''
            #!/bin/bash
            set -e

            echo "Checking for Python..."
            if ! command -v python3 &> /dev/null; then
                echo "❌ Python3 not found and cannot install (no sudo)."
                echo "⚠️ Please install python3, python3-venv, and python3-pip in the Jenkins container manually."
                exit 1
            fi

            echo "✅ Python3 found: $(python3 --version)"

            echo "Creating virtual environment..."
            python3 -m venv venv || echo "⚠️ Could not create venv (maybe missing venv module). Skipping..."
            
            if [ -f venv/bin/activate ]; then
                . venv/bin/activate
                echo "Upgrading pip..."
                pip install --upgrade pip

                if [ -f requirements.txt ]; then
                    echo "Installing dependencies..."
                    pip install -r requirements.txt
                else
                    echo "⚠️ No requirements.txt found, skipping dependencies."
                fi
            else
                echo "⚠️ Virtual environment not created. Running without venv."
                if [ -f requirements.txt ]; then
                    pip3 install -r requirements.txt || echo "⚠️ Could not install dependencies."
                fi
            fi
        '''
    }

    stage('Run Tests') {
        echo 'Running tests...'
        sh '''
            #!/bin/bash
            set +e
            if [ -f venv/bin/activate ]; then
                . venv/bin/activate
            fi
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
