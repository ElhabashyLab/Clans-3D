from clans3d.legacy.utils_old_clans import *
import sys

if __name__ == "__main__":
    args = sys.argv
    
    if len(args) != 4:
        print("Usage: python generate_seq_based_clans_file.py <fasta_file_path> <out_dir_path> <blast_work_dir_path>")
        sys.exit(1)
        
    fasta_file_path = args[1]
    out_dir_path = args[2]
    blast_work_dir_path = args[3]
    clans_file_path = generate_clans_file_seq_based(fasta_file_path, out_dir_path, blast_work_dir_path)
    print(f"Generated clans file: {clans_file_path}")
