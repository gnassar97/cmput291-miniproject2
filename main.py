import parser
import indexing
import query

def main():
    parser.create_parsed_files()
    indexing.create_idx_files()
    query.options_interface()

main()


