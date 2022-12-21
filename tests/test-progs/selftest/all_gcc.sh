#! /bin/bash

gcc src/$1 -o bin/x86/$2 -std=gnu99 -static
echo "x86:    gcc return $?";

aarch64-none-linux-gnu-gcc src/$1 -o bin/arm/$2 -std=gnu99 -static
echo "arm:    gcc return $?";

riscv64-unknown-linux-gnu-gcc src/$1 -o bin/riscv/$2 -std=gnu99 -static
echo "riscv:  gcc return $?";