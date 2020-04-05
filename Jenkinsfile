pipeline{
        agent any
        stages{
            stage('Deploy Application'){
                steps{
                    sh """
                    ssh zreginaldoz@51.104.32.229 << EOF
                    rm -rf PracticalSFIAProject
                    git clone https://github.com/zReginaldo/PracticalSFIAProject.git
                    cd PracticalSFIAProject
                    export Version=v2
                    docker stack deploy --compose-file docker-compose.yaml flaskapp
                    echo ${Version}
                    """
               }
            }
        }    
}
