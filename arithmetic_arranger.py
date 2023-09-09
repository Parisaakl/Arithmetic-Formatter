def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize lists to store components of each problem
    first_operand = []
    second_operand = []
    operator = []

    # Extract and separate first operands, operators, and second operands from input
    for problem in problems:
        pieces = problem.split()
        first_operand.append(pieces[0])
        operator.append(pieces[1])
        second_operand.append(pieces[2])

    # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Check if all operands are digits
    for i in range(len(first_operand)):
        if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check if operands are not more than four digits long
    for i in range(len(first_operand)):
        if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Initialize lists to store formatted lines for each component
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    # Format the first line with appropriate spacing
    for i in range(len(first_operand)):
        if len(first_operand[i]) > len(second_operand[i]):
            first_line.append(" "*2 + first_operand[i])
        else:
            first_line.append(" "*(len(second_operand[i]) - len(first_operand[i]) + 2) + first_operand[i])

    # Format the second line with appropriate spacing
    for i in range(len(second_operand)):
        if len(second_operand[i]) > len(first_operand[i]):
            second_line.append(operator[i] + " " + second_operand[i])
        else:
            second_line.append(operator[i] + " "*(len(first_operand[i]) - len(second_operand[i]) + 1) + second_operand[i])

    # Create the third line with dashes
    for i in range(len(first_operand)):
        third_line.append("-"*(max(len(first_operand[i]), len(second_operand[i])) + 2))

    if answer:
        # Calculate and format the answers if required
        for i in range(len(first_operand)):
            if operator[i] == "+":
                ans = str(int(first_operand[i]) + int(second_operand[i]))
            else:
                ans = str(int(first_operand[i]) - int(second_operand[i]))

            # Format the answer line with appropriate spacing
            if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        # Combine all lines without answers
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems
