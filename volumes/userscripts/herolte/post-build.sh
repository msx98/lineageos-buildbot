BRANCH_DIR=${BRANCH_NAME//[^[:alnum:]]/_}
BRANCH_DIR=${BRANCH_DIR^^}
REPO_DIR="${SRC_DIR}/${BRANCH_DIR}"
sh /srv/patches/revert.sh /srv/patches $REPO_DIR
