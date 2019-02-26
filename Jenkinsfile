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
                withDockerRegistry([url: "http://${NEXUS_RAW_RELEASE_REPO}", credentialsId: "8258d105-ddf8-43bc-8714-00718fe2cedc"]){
                    sh '''
                        docker build -t ${NEXUS_APP_RELEASE_REPO}/${APP_IMAGE_NAME} -f Dockerfile .
                    '''
                }
            }
        }
        stage('Push image to Application Repo'){
            steps{
                withDockerRegistry([url: "http://${NEXUS_APP_RELEASE_REPO}", credentialsId: "8258d105-ddf8-43bc-8714-00718fe2cedc"]){
                    sh '''
                        docker push ${NEXUS_APP_RELEASE_REPO}/${APP_IMAGE_NAME}
                    '''
                }
            }

        }
        stage('Deploy Application to minikube'){
            steps{
                   sh'''
                      #Create config file 
                       mkdir ~/.kube
                       echo "echo "apiVersion: v1
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
    client-key: /home/.minikube/client.key" > ~/.kube/config
            
                   # apply yaml file
                   kubectl apply -f kubernetes/python-redis-deployment.yaml 
                   '''

            }
       } 


    }


}
