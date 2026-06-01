#!/bin/bash

awk -F',' '
NR>1 {
    tong += $2
}
END {
    print "Tong doanh thu =", tong
}' doanhso.csv
