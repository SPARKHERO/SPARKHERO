pipeline {
    agent any
    environment {
        SECRET_ID="Hero@17569"
        JENKINS_USER_PREVIEW="hduser"
        JENKINS_USER_VALIDATION="hduser"
        JENKINS_USER_PRODUCTION="hduser"

        APP_ROOT_PREVIEW="/home/hduser/jenkins/preview"
        APP_ROOT_VALIDATION="/home/hduser/jenkins/validation"
        APP_ROOT_PRODUCTION="/home/hduser/jenkins/production"

        RELEASE="Jenkins_Testing_${env.BUILD_ID}"

        HOST_PREVIEW="DESKTOP-NC44LBV"
        HOST_VALIDATION="DESKTOP-NC44LBV"
        HOST_PRODUCTION="DESKTOP-NC44LBV"

        LINKNAME="Jenkins_Testing"

        TAR_NAME="test.tar.gz"

        EMAIL_FROM="hui.huang.stephen@gamil.com"
        EMAIL_TO="hui.huang.stephen@gamil.com"


    }
    stages {
        stage ('Check out') {
            steps {
                sh "echo Checking out ......."

                sh "echo ===============================1"
                sh "echo ${env.BUILD_ID}"
                sh "echo ${env.GIT_BRANCH}"
                sh "echo ===============================2"
                checkout scm
                sh "touch ${TAR_NAME}"
                sh "tar --exclude-vcs --exclude='*.gz' --exclude='*jenkin*' -czvf ${TAR_NAME}"
                sh "pwd"
                sh "ls -lart"
            }
        }

        stage ('Deployment preview') {
            when {
                expression {env.GIT_BRANCH == 'preview'}
            }
                steps {
                    withCredentials([sshUserPrivateKey(credentialsId:SECRET_ID, keyFileVariable: 'sshKey')]) {
                        sh "echo Deploying preview branch"
                        sh "${sshKey}"
                        sh "echo ===============================2"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'mkdir /tmp/${RELEASE}/'"
                        //sh "scp -v -i ${sshKey} *.gz ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW}:/tmp/${RELEASE}/.'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'cp -pr /tmp/${RELEASE} ${APP_ROOT_PREVIEW}/.'"

                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'ln -sfn ${APP_ROOT_PREVIEW}/${RELEASE}/ ${APP_ROOT_PREVIEW}/${LINKNAME}'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'tar -xhzvf ${APP_ROOT_PREVIEW}/${LINKNAME}/${TAR_NAME} -C ${APP_ROOT_PREVIEW}/${LINKNAME}/'"
                        ////sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'rm -r /tmp/${RELEASE}/'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'chmod 755 -R ${APP_ROOT_PREVIEW}/${LINKNAME}/*'"
                    }
                }
        }


        stage ('Deployment Validation') {
            when {
                expression {env.GIT_BRANCH == 'origin/preview'}
            }
                steps {
                    withCredentials([sshUserPrivateKey(credentialsId:SECRET_ID, keyFileVariable: 'sshKey')]) {
                        sh "echo Deploying validation branch"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION} 'mkdir /tmp/${RELEASE}/'"
                        sh "scp -v -i ${sshKey} *.gz ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION}:/tmp/${RELEASE}/.'"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION} 'cp -pr /tmp/${RELEASE} ${APP_ROOT_VALIDATION}/.'"

                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION} 'ln -sfn ${APP_ROOT_VALIDATION}/${RELEASE}/ ${APP_ROOT_VALIDATION}/${LINKNAME}'"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION} 'tar -xhzvf ${APP_ROOT_VALIDATION}/${LINKNAME}/${TAR_NAME} -C ${APP_ROOT_VALIDATION}/${LINKNAME}/'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION} 'rm -r /tmp/${RELEASE}/'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_VALIDATION}@${HOST_VALIDATION} 'rm ${APP_ROOT_VALIDATION}/${LINKNAME}/*.gz'"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'chmod 755 -R ${APP_ROOT_PREVIEW}/${LINKNAME}/*'"
                    }
                }
        }


        stage ('Deployment Production') {
            when {
                expression {env.GIT_BRANCH == 'origin/master'}
            }
                steps {
                    withCredentials([sshUserPrivateKey(credentialsId:SECRET_ID, keyFileVariable: 'sshKey')]) {
                        sh "echo Deploying master branch"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION} 'mkdir /tmp/${RELEASE}/'"
                        sh "scp -v -i ${sshKey} *.gz ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION}:/tmp/${RELEASE}/.'"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION} 'cp -pr /tmp/${RELEASE} ${APP_ROOT_PRODUCTION}/.'"

                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION} 'ln -sfn ${APP_ROOT_PRODUCTION}/${RELEASE}/ ${APP_ROOT_PRODUCTION}/${LINKNAME}'"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION} 'tar -xhzvf ${APP_ROOT_PRODUCTION}/${LINKNAME}/${TAR_NAME} -C ${APP_ROOT_PRODUCTION}/${LINKNAME}/'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION} 'rm -r /tmp/${RELEASE}/'"
                        //sh "ssh -v -i ${sshKey} ${JENKINS_USER_PRODUCTION}@${HOST_PRODUCTION} 'rm ${APP_ROOT_PRODUCTION}/${LINKNAME}/*.gz'"
                        sh "ssh -v -i ${sshKey} ${JENKINS_USER_PREVIEW}@${HOST_PREVIEW} 'chmod 755 -R ${APP_ROOT_PREVIEW}/${LINKNAME}/*'"
                    }
                }
        }


    }

    post {
        always { echo "This will always run" }
        success {
            echo 'The build is successful'
            emailext body: "Project: ${JOB_NAME} <br>Build Number: ${BUILD_NUMBER} <br> URL DE BUILD: ${BUILD_URL}",
                from: "${EMAIL_FROM}",
                mimeType: "text/html",
                attachLog: true,
                replyTo: "",
                subject: "ERROR CI: Project Name -> ${JOB_NAME}",
                to: "${EMAIL_TO}";
        }

        failure {
            echo 'The build is failed'
            emailext body: "Project: ${JOB_NAME} <br>Build Number: ${BUILD_NUMBER} <br> URL DE BUILD: ${BUILD_URL}",
                from: "${EMAIL_FROM}",
                mimeType: "text/html",
                attachLog: true,
                replyTo: "",
                subject: "ERROR CI: Project Name -> ${JOB_NAME}",
                to: "${EMAIL_TO}";
        }

        unstable {echo "This will run only if the run was marked as unstable"}

        changed {echo "The build is back to normal"}
    }
}

