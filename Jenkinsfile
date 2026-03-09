pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['all', 'api', 'ui'],
            description: 'Какие тесты запустить?'
        )
    }

    stages {
        stage('Установка зависимостей') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('API тесты') {
            when {
                expression { params.TEST_SUITE in ['all', 'api'] }
            }
            steps {
                sh 'pytest tests/api/ -v --junitxml=reports/api.xml'
            }
        }

        stage('UI тесты') {
            when {
                expression { params.TEST_SUITE in ['all', 'ui'] }
            }
            steps {
                sh 'pytest tests/ui/ -v --junitxml=reports/ui.xml'
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
        }
    }
}