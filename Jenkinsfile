pipeline{
    agent{
        label 'docker-worker'
    }
    environment{
        APP_IMAGE_NAME="hello-python:1.0.0"
        NEXUS_RAW_RELEASE_REPO='127.0.1.1:7502'
        NEXUS_APP_RELEASE_REPO='127.0.1.1:7505'
    }

    stages{
        stage('Build application image'){
            steps{
                withDockerRegistry([url: "http://${NEXUS_RAW_RELEASE_APP}", credentialsId: "8258d105-ddf8-43bc-8714-00718fe2cedc"]){
                    sh '''
                        docker build -t ${NEXUS_APP_RELEASE_REPO}/${APP_IMAGE_NAME} -f Dockerfile
                    '''
                }
            }
        }
    }


}