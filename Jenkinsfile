pipeline {
    agent any
    triggers {
        pollSCM("* * * * *")
    }
    stages {
        stage("Unit Test") {
            steps {
                sh "python3 test_calculator.py"
            }
        }
    }
}