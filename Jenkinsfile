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
       
        
    }
}	