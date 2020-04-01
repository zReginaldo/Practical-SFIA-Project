pipeline{
        agent any
        stages{
            stage('Ssh In'){
                steps{
                      sh """
                    ssh -i ~/id_rsa zreginaldoz@51.104.32.229 <<EOF
                    ls 
                    pwd
                    """
                }
            }
            stage ('Remove Git repo if it exists'){
                steps{
                    sh """
                    rm -rf Inital_Mvp
                    mkdir Initial_Mvp
                    """
                }
            }
            stage('Create New Updated repo'){
                steps{
                    sh """
                    cd Initial_Mvp
                    git init
                    git clone https://github.com/zReginaldo/PracticalSFIAProject.git
                    cd PracticalSFIAProject
                    """
                }
            }
            stage ('Deploy Application'){
                steps{
                    sh """
                    docker stack deploy --compose-file docker-compose.yaml flaskapp
                    """
               }
            }
        }    
}