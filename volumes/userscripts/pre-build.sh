REPO_DIR=$SRC_DIR/LINEAGE_19_1
PATCHES_DIR=/srv/patches

cd $REPO_DIR
bash $PATCHES_DIR/picks.sh

echo Applying hardware/libhardware
cd $REPO_DIR
cp $PATCHES_DIR/patches/hardware/libhardware/* hardware/libhardware
cd hardware/libhardware
git apply *.patch

echo Applying system/bpf
cd $REPO_DIR
cp $PATCHES_DIR/patches/system/bpf/* system/bpf
cd system/bpf
git apply *.patch

echo Applying system/netd
cd $REPO_DIR
cp $PATCHES_DIR/patches/system/netd/* system/netd
cd system/netd
git apply *.patch

echo Applying system/security
cd $REPO_DIR
cp $PATCHES_DIR/patches/system/security/* system/security
cd system/security
git apply *.patch

