#!/usr/bash

mfab() {
    hosts=()
    while [ "$#" != 0 ]; do
        if [ "$1" = -- ]; then
            shift
            break
        fi
        hosts+=("$1")
        shift
    done

    list=$(echo "${hosts[@]}" | tr ' ' ',')
    fab -H "$list" "$@"
}
