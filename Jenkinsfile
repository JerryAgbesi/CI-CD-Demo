pipeline {
  agent any

    stages{

        stage("run migrations"){
            steps{
                sh "echo 'not ready'" 
            }
        }

        stage("Build"){
            steps{
                sh "docker build . -t ci-cd-demo:v1" 
            }
        }
    }

}