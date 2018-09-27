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
        sh '''ls
pwd'''
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