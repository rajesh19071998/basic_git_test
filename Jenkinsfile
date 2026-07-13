pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull latest code from GitHub
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']],
                          userRemoteConfigs: [[url: 'https://github.com/rajesh19071998/basic_git_test.git']]
                ])
            }
        }

        stage('Build') {
            steps {
                // Build firmware using PlatformIO from Jenkins venv
                sh '/var/lib/jenkins/pio-venv/bin/pio run -e esp32dev'
            }
        }

        stage('Upload') {
            steps {
                // Upload firmware to ESP32 board
                // sh '/var/lib/jenkins/pio-venv/bin/pio run -e esp32dev -t upload'
                echo 'Upload code to board'
            }
        }

        stage('Setup venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=results.xml
                '''
            }
        }
        stage('Publish Report') {
            steps {
                junit 'results.xml'
            }
        }

        stage('Archive Firmware') {
            steps {
                archiveArtifacts artifacts: ".pio/build/esp32dev/*.bin", fingerprint: true
            }
        }

        stage('Cleanup') {
            steps {
                echo '🧹 Cleaning up cloned repo...'
                // Delete the cloned repo
                sh 'rm -rf ${WORKSPACE}/basic_git_test'
                //sh 'rm -rf ${WORKSPACE}/basic_git_test'
                sh 'rm -rf ${WORKSPACE}'
            }
        }
    }

    post {
        success {
            echo '✅ Build and upload completed successfully!'
            emailext(
                subject: "✅ ESP32 Build Success",
                body: "The build and upload completed successfully.\nCheck Jenkins for details.",
                //to: "your_email@example.com"
                to: "rajeshnodemcu@gmail.com"
            )
        }
        failure {
            echo '❌ Build failed. Check logs for details.'
            emailext(
                subject: "❌ ESP32 Build Failed",
                body: "The build failed. Please check Jenkins logs for details.",
                //to: "your_email@example.com"
                to: "rajeshnodemcu@gmail.com"
            )
        }
    }
}