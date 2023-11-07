#! /bin/bash

arg="$1"
var1="parse"
var2="clean"

declare -a files
input_dir="testcases_input"
output_dir="testcases_output"

cd $input_dir
files=( $( ls . ) )
cd ../	
if [[ "$arg" == "$var1" ]]; then
	rm -rf $output_dir
	mkdir $output_dir
	for file in "${files[@]}"
	do
		output_file="${output_dir}/${file%.*}.txt"
		python3 main.py < "${input_dir}/${file}" > "${output_file}"
		echo "Generated file: ${output_file}"
	done
	
elif [[ "$arg" == "$var2" ]]; then
	echo "removing files"
    rm -rf parser.out
    rm -rf parsetab.py
	rm -rf $output_dir

else
	echo "valid commands are: parse or clean"
fi
