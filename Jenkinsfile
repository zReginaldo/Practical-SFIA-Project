pipeline{
    agent any
	environment
	{
		build = "${env.Version}"
	}
	stages{
		stage("Update git repository") {
			steps{sh '''
                sudo su - jenkins
                cd Practical-SFIA-Project
                git pull
                echo "${build}"
                '''
			}
		}
		stage("Build") {
			steps{sh '''
                sudo su - jenkins
                cd Practical-SFIA-Project
                export Version="${build}"
                docker-compose build
                docker-compose push
                '''
			}
		}
		stage("Deploy") {
			steps{sh '''ssh flaskapp << EOF
                sudo su - jenkins
                cd Practical-SFIA-Project
                git pull
                export Version="${build}"
                #scp ./nginx/nginx.conf
                docker stack deploy --compose-file docker-compose.yaml stack
                '''
			}
		}
	}
}