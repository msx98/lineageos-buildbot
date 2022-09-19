REPODIR=$SRC_DIR/LINEAGE_19_1
cd $REPODIR
bash $REPODIR/patches/picks.sh

echo Applying hardware/libhardware
cd $REPODIR
cp patches/patches/hardware/libhardware/* hardware/libhardware
cd hardware/libhardware
git apply *.patch

echo Applying system/bpf
cd $REPODIR
cp patches/patches/system/bpf/* system/bpf
cd system/bpf
git apply *.patch

echo Applying system/netd
cd $REPODIR
cp patches/patches/system/netd/* system/netd
cd system/netd
git apply *.patch

echo Applying system/security
cd $REPODIR
cp patches/patches/system/security/* system/security
cd system/security
git apply *.patch

