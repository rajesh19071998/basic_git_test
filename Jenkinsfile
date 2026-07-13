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
            parallel {
                stage('esp32dev') {
                    steps {
                        // Build firmware for ESP32 (esp32dev environment)
                        sh '/var/lib/jenkins/pio-venv/bin/pio run -e esp32dev'
                    }
                }
                stage('nodemcu') {
                    steps {
                        // Build firmware for NodeMCU (nodemcu environment)
                        sh '/var/lib/jenkins/pio-venv/bin/pio run -e nodemcu'
                    }
                }
            }
        }

        stage('Upload') {
            steps {
                // Upload firmware to ESP32 board
                // sh '/var/lib/jenkins/pio-venv/bin/pio run -e esp32dev -t upload'
                echo 'Upload code to board'
            }
        }
        
        stage('Archive Firmware') {
            steps {
                // Archive binaries for both build environments
                archiveArtifacts artifacts: ".pio/build/esp32dev/*.bin, .pio/build/nodemcu/*.bin", fingerprint: true
            }
        }

        stage('Cleanup') {
            steps {
                echo '🧹 Cleaning up cloned repo...'
                // Delete the cloned repo
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
