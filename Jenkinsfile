// @Library('shared-libraries')

pipeline {
  agent any

  environment {
        imagename = "jerryelikem/ci-cd-demo:latest"
    }

  stages{

        stage("Run tests"){
            steps{
                 withCredentials([file(credentialsId: 'CI-Env-File',variable: 'ENV_FILE')]){
                    script {
                        sh "cp $ENV_File .env"
                        sh "pytest --disable-warnings tests/test_books.py" 

                    }
        }
               
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

        // stage("Build image"){
        //     steps{
        //         sh "docker build . -t ${imagename}" 
        //     }
        // }

        // stage("Push image to DockerHub registry"){
        //     steps{
        //          script {
                   
        //             withCredentials([
        //                 usernamePassword(credentialsId: "demoDockerHubCredentials", 
        //                 usernameVariable: 'DOCKER_USERNAME', 
        //                 passwordVariable: 'DOCKER_PASSWORD')]) {
        //                 sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
 
                       
        //                 sh "docker push ${imagename}"
        //             }
        //     }

        //     }
        // }

    //     stage("Trigger redeploy on Render"){
    //         steps{
    //             withCredentials([string(credentialsId: 'redeployURL',variable: 'redeployURL')]){
    //                       sh "curl $redeployURL"
    //         }
    //     }
    // }
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