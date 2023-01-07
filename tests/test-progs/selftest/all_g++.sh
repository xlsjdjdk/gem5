#! /bin/bash

g++ src/$1 -o bin/x86/$2 -std=c++11 -static
echo "x86:    g++ return $?";

aarch64-linux-gnu-g++ src/$1 -o bin/arm/$2 -std=c++11 -static
echo "arm:    g++ return $?";

riscv64-unknown-linux-gnu-g++ src/$1 -o bin/riscv/$2 -std=c++11 -static
echo "riscv:  g++ return $?";