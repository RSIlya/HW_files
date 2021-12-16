
def count_line_in_file(file):
    with open(file, encoding='utf-8') as f:
        count_line = len(f.readlines())
    return count_line

def merge_sorted_files(output_file, *input_files):
    count_len_line = {}
    for file in input_files:
        count_len_line[file] = count_line_in_file(file)
    sorted_files = sorted(count_len_line, key=count_len_line.get)
    with open(output_file, 'w') as output:
        for file in sorted_files:
            output.write(file + '\n')
            output.write(str(count_len_line[file]) + '\n')
            with open(file, encoding='utf-8') as merged_file:
                output.write(merged_file.read())
             
    
merge_sorted_files('output.txt', '1.txt', '2.txt', '3.txt')

with open('output.txt') as f:
    print(f.read())
