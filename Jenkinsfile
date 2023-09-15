pipeline {
	agent any
	stages {
		stage('Build') {
			steps {
				echo "Building the code"
				sh 'docker image build -t ashish56/devops_demo:v2.$BUILD_NUMBER .'
			}
		}
		stage('DeployStaging') {
			steps {
				echo "Deploying to staging env"
				sh 'docker container stop myapp || true'
				sh 'docker container rm myapp ||true'
				echo "Building docker container"
				sh 'docker container run -d --name myapp -p 8072:8071 ashish56/devops_demo:v2.$BUILD_NUMBER'
			}
		}
		stage('DeploytoProd'){
			steps {
				timeout(time:1, unit:'DAYS'){
				input message:'Approve PRODUCTION Deployment?'
				}
				echo "Deploying to prod env"
				sh '''
				docker container stop myapp || true
				docker container rm myapp || true
				docker container run -d --name myapp -p 8073:8071 ashish56/devops_demo:v2.$BUILD_NUMBER
				'''
			}
		}
	}
	post {
		always {
			echo "Post stage..."
		}
		failure {
			echo "Job failed"
		}
		success {
			echo "Job ran successfully"
			sh 'docker push ashish56/devops_demo:v2.$BUILD_NUMBER'
		}
	}
}
