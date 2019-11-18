pipeline { 
     environment {
        registry = "arig23498/inframind-web"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
        stage ('Initialize') {
            steps {
                sh '''
                    echo "PATH = ${PATH}"
                    echo "M2_HOME = ${M2_HOME}"
                    pwd
                    ls -al
                ''' 
            }
        }
        stage('Docker Push') { 
            steps { 
               script{
                    dockerImage = docker.build registry
               }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                        docker.withRegistry( '', registryCredential ) {
                                dockerImage.push("$BUILD_NUMBER")
        				        dockerImage.push("latest")
                            }
                        }
                }
        }
        stage ('Kubernetes Deployment') {
            steps {
                script {
                def remote  = [:]
                remote.name = "Test03"
                remote.host = "10.134.19.203"
                remote.user = "user"
                remote.password = "tcs#1234"
                remote.allowAnyHosts = true
                sshCommand remote: remote, command: "kubectl apply check.yaml"
                }
            }
        }
        stage('Pod health check') {
            steps {
                script {
                    def remote  = [:]
                    remote.name = "Test06"
                    remote.host = "10.134.19.206"
                    remote.user = "user"
                    remote.password = "tcs#1234"
                    remote.allowAnyHosts = true
                    numPods = sshCommand remote, command: "kubectl get pods | grep Running | wc -l"
                    echo "$numPods"
                    if (numPods == 0) {
                        // deploy to cluster velachery
                    } else {
                        def remote_velachery = [:]
                        remote_velachery.name = "Test08"
                        remote_velachery.host = "10.134.19.208"
                        remote_velachery.user = "user"
                        remote_velachery.password = "tcs#1234"
                        sshCommand remote_velachery, command: "kubectl run --image=drake666/inframind-finale:latest inframind-finale-v$BUILD_NUMBER --port=9090 --replicas=2"
                    }

                }
            }
        }
    }
}	