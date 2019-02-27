pipeline{
    agent{
        label 'docker-worker'
    }
    environment{
        DOCKER_REPO="docuser200" 
        APP_IMAGE_NAME="python-webapp:${BUILD_NUMBER}.0.0"
        DOCKERHUB_REGISTRY="https://index.docker.io" 
    }

    stages{
        stage('Build application image'){
            steps{
        //        withDockerRegistry([url: "http://${NEXUS_RAW_RELEASE_REPO}", credentialsId: "8258d105-ddf8-43bc-8714-00718fe2cedc"]){
                    sh '''
                        docker build -t ${DOCKER_REPO}/${APP_IMAGE_NAME} -f Dockerfile .
                    '''
         //       }
            }
        }
        stage('Push image to Application Repo'){
            steps{
                withDockerRegistry([url: "${DOCKERHUB_REGISTRY}", credentialsId: "fb81a327-08b9-43f6-9e8e-95d99d7d01ed"]){
                    sh '''
                        docker push ${DOCKER_REPO}/${APP_IMAGE_NAME}
                    '''
                }
            }

        }
        
        stage('Update image name in yaml'){
           steps{
                  sh'''
                   sed -i "s/IMAGE_NAME/${DOCKER_REPO}\\/${APP_IMAGE_NAME}/g"  kubernetes/python-webapp-deployment.yaml
                   cat kubernetes/python-webapp-deployment.yaml 
                  '''
           }

        }
        stage('Deploy Application to minikube'){
            steps{
                   sh'''
                      #Create config file 
                       mkdir ~/.kube
                       echo 'apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/.minikube/ca.crt
    server: https://192.168.99.100:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /home/.minikube/client.crt
    client-key: /home/.minikube/client.key' > ~/.kube/config
            
                   # apply yaml file
                   kubectl apply -f kubernetes/python-redis-deployment.yaml 
                   
                   kubectl apply -f kubernetes/python-webapp-deployment.yaml
                   '''

            }
       } 
       stage('Cleanup images from host') {
           steps { 
                    sh'''
                         docker rmi ${DOCKER_REPO}/${APP_IMAGE_NAME} 
                    '''
           } 
       }
   

    }


}
