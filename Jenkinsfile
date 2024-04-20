pipeline {
    agent {
        docker { image "salaichitoolatt/jenkins-agent-python"}
    }
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