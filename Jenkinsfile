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
				sh 'docker container stop mystagingapp || true'
				sh 'docker container rm mystagingapp ||true'
				echo "Building docker container"
				sh 'docker container run -d --name mystagingapp -p 8072:8071 ashish56/devops_demo:v2.$BUILD_NUMBER'
			}
		}
		stage('DeploytoProd'){
			steps {
				timeout(time:1, unit:'DAYS'){
				input message:'Approve PRODUCTION Deployment?'
				}
				echo "Deploying to prod env"
				sh '''
				docker container stop myprodapp || true
				docker container rm myprodapp || true
				docker container run -d --name myprodapp -p 8073:8071 ashish56/devops_demo:v2.$BUILD_NUMBER
				'''
			}
		}
	}
	post {
		always {
			mail to: 'maharjanashish96@gmail.com',
			subject: "Job '${JOB_NAME}' (${BUILD_NUMBER}) is waiting for input",
			body: "Please go to ${BUILD_URL} and verify the build"
		}
		failure {
			echo "Job failed"
			mail bcc: '', body: """
			Hello User,
			
			Build #$BUILD_NUMBER is unsuccessful, please go through the url

			$BUILD_URL
			and verify the details.

			Regards,
			Jenkins
			""",
			cc: '', from: '', replyTo: '', subject: 'BUILD SUCESS NOTIFICATION',
                        to: 'maharjanashish96@gmail.com'
		}
		success {
			echo "Job ran successfully"
			sh 'docker push ashish56/devops_demo:v2.$BUILD_NUMBER'
			
			mail bcc: '', body: """
			Hello User,
			
			Build #$BUILD_NUMBER is successful, please go through url
			$BUILD_URL
			and verify the details.

			Regards,
			Jenkins
			""",
			cc: '', from: '', replyTo: '', subject: 'BUILD SUCESS NOTIFICATION',
			to: 'maharjanashish96@gmail.com'
		}
	}
}
