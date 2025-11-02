node {
    stage('Checkout') {
        git branch: 'main', url: 'https://github.com/Samikaa7/chef_cart_ms_new.git'
    }

    stage('Build & Test inside Python container') {
        // Run everything inside a Docker container that has Python preinstalled
        docker.image('python:3.9').inside('-u root') {
            stage('Setup Environment') {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "⚠️ No requirements.txt found, skipping dependency installation."
                    fi
                '''
            }

            stage('Test') {
                sh '''
                    . venv/bin/activate
                    if [ -f test_script.py ]; then
                        python3 test_script.py
                    else
                        echo "⚠️ No test_script.py found, skipping tests."
                    fi
                '''
            }

            stage('Package') {
                sh '''
                    mkdir -p dist
                    cp -r * dist/
                    echo "✅ Packaging complete."
                '''
            }
        }
    }

    stage('Post Build') {
        echo '✅ Build completed successfully.'
    }
}
