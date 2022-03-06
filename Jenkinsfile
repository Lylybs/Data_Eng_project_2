pipeline {
  agent any
  stages {
    stage('pytest') {
      steps {
        sh 'python -m pytest'
        git(url: 'https://github.com/Lylybs/Data_Eng_project_2.git', branch: 'test_app')
      }
    }

  }
}