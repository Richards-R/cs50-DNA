import csv
import sys
# from pprint import pprint


def main():

    rows = []

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print('USAGE: python dna.py databases/(dbase_filename).csv sequences/(sequence_filename).txt')
        sys.exit()

    # TODO: Read database file into a variable
    else:
        with open(sys.argv[1]) as file:
            db_file_reader = csv.DictReader(file)
            field_names = db_file_reader.fieldnames
            for row in db_file_reader:
                rows.append(row)
            # pprint(rows)

    # TODO: Read DNA sequence file into a variable
        with open(sys.argv[2]) as file:
            seq_text = file.read()

    # TODO: Find longest match of each STR in DNA sequence
        field_names = field_names[1:]
        result_list = {}

        for str in field_names:
            result = longest_match(seq_text, str)
            result_list[str] = result
        # print(result_list)

    # TODO: Check database for matching profiles
        str_count = len(result_list)

        for row in rows:
            match_count = 0
            for str in row:
                for res_str in result_list:
                    res_list_val = result_list[res_str]
                    row_list_val = row[str]
                    if res_str == str and res_list_val == int(row_list_val):
                        match_count += 1

                        if match_count == str_count:
                            print(f"{row['name']}")
                            return

        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
