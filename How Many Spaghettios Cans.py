import string


def main():
    # initialize the arrays and other variables that will be used
    letters = list(string.ascii_uppercase)

    with open('bee-movie-script.txt', 'r') as f:
        lines = f.readlines()
        alpha_lines = ""
        for line in lines:
            for i in range(len(line)):
                alpha_line = ""
                if line[i].isalpha():
                    alpha_line += line[i]
                alpha_lines += alpha_line

        alpha_lines = alpha_lines.lower()

        all_freq = {}

        for i in alpha_lines:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1

        x = list(map(int, input("Number of letters A-Z (separated by spaces): ").split()))
        # sample number of letters A-Z, comment out later
        #x = [17, 29, 30, 42, 53, 39, 23, 24, 20, 98, 83, 28, 49, 31, 85, 50, 23, 52, 45, 37, 43, 57, 95, 84, 89, 32]

        while len(x) != 26:
            print("Incorrect number of letters! You have ", len(x), "letters!")
            x = list(map(int, input("Number of letters A-Z (separated by spaces): ").split()))

        print("Number of letters A-Z: ", x)

        min_num_cans = 0

        for i, j in enumerate(string.ascii_lowercase):
            if all_freq[j] / x[1] > min_num_cans:
                min_num_cans = all_freq[j] / x[1]

        min_num_cans = min_num_cans.__ceil__()
        print(min_num_cans)

        f.close()


main()
