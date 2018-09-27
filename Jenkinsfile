pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
        sh '''cd .. 
source venv/bin/activate
which python'''
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
        echo 'Finished deploying'
      }
    }
  }
}