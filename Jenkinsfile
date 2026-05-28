pipeline {
    agent any

    stages {

        stage('GitHub Clone') {
            steps {
                echo 'Cloning Project'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run FastAPI App') {
            steps {
                echo 'Running Weather API'
            }
        }

        stage('MLflow Execution') {
            steps {
                bat 'python mlflow_demo.py'
            }
        }

    }
}