pipieline {
	agent any
	stages {
		stage('UnitTest') {
			steps {
				echo "This is the jenkins pipeline"
				echo "Running Unit test"
			}
		stage('Build') {
			steps {
				echo "Building the code"
			}
		}
		stage('DeployStaging') {
			steps {
				echo "Deploying to staging env"
				}
			}
		stage('DeploytoProd'){
			steps {
				echo "Deploying to prod env"
				}
			}_	
		}
	}
}
