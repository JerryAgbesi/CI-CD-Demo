// @Library('shared-libraries')

pipeline {
  agent any

  environment {
        imagename = "jerryelikem/ci-cd-demo:latest"
    }

  stages{

        stage("run migrations"){
            steps{
                sh "echo 'not ready'" 
            }
        }

        stage("Static code analysis"){
            steps{
                withSonarQubeEnv('SonarQube') {
                    script {
                        def scannerHome = tool 'SonarScanner'
                        sh "${scannerHome}/bin/sonar-scanner"
                            }
                }
            }
        }

        stage("Build image"){
            steps{
                sh "docker build . -t ${imagename}" 
            }
        }

        stage("Push image to registry"){
            steps{
                 script {
                    // Use Jenkins credentials for Docker Hub login
                    withCredentials([
                        usernamePassword(credentialsId: "demoDockerHubCredentials", 
                        usernameVariable: 'DOCKER_USERNAME', 
                        passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
 
                        // Push the image
                        sh "docker push ${imagename}"
                    }
            }

            }
        }

        stage("Trigger redeploy on Render"){
            steps{
                withCredentials([string(credentialsId: 'redeployURL',variable: 'redeployURL')]){
                          sh "curl $redeployURL"
            }
        }
    }
  }
  
  post{
        always{
            script {
                try {
                    sh "docker rmi ${imagename}"
                    sh 'docker system prune -f'
                    cleanWs()
                } catch (Exception e) {
                    echo "Cleanup failed: ${e.getMessage()}"
                }
            }
        }
    }

}