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
        sh '''cd ../venv/bin
source activate
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