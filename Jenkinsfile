pipeline{
        agent any
        stages{
            stage('Deploy Application'){
                steps{
                      sh """
                    ssh -i ~/id_rsa zreginaldoz@51.104.32.229 <<EOF
                    ls 
                    pwd
                    rm -rf Inital_Mvp
                    mkdir Initial_Mvp
                    cd Initial_Mvp
                    git init
                    git clone https://github.com/zReginaldo/PracticalSFIAProject.git
                    cd PracticalSFIAProject
                    docker stack deploy --compose-file docker-compose.yaml flaskapp
                    """
               }
            }
        }    
}