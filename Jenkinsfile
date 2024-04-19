pipeline {
    agent any
    triggers {
        pollSCM("* * * * *")
    }
    stages {
        stage("Unit Test") {
            steps {
                sh "python test_calculator.py"
            }
        }
    }
}