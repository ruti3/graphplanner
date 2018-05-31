import sys

#parameters
# opposite of what we have, everything is oppsitie:
# if we have all of the disks on first pile that for us meaning they arent on piles 2 and 3.
# but we implemented it as they are on piles 2 and 3 just not on 1.
#actions
#move a from pile to pile

def create_domain_file(problem_file_name_, n_, m_):
    domain_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    # Propososition
    domain_file.write("Propositions:\n")

    for disk in range(n_):
        for pile in range(m_):
            domain_file.write(proposition(disk, pile))

    #actions :
    domain_file.write("\nActions:\n")

    for disk in range(n_):
        for pile in range(m_):
            for to_pile in range(m_):
                if not pile == to_pile:
                    move(disk, pile, to_pile, domain_file)
    domain_file.close()

def proposition(disk, piles):
    return "n" + str(disk) + "m" + str(piles) + " "

def move(disk, from_pile, to_pile, domain_file):

  # Name
    domain_file.write("Name: Mn" + str(disk) + "m" + str(from_pile) + str(to_pile) + '\n')
  # pre
    domain_file.write("pre: " + proposition(disk, to_pile))
    for i in range(disk):
        domain_file.write(proposition(i, from_pile) + proposition(i, to_pile))
  # add
    domain_file.write("\nadd: " + proposition(disk, from_pile) + '\n')
  # delete
    domain_file.write("delete: " + proposition(disk, to_pile) + '\n')


def create_problem_file(problem_file_name_, n_, m_):
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file

  # Initial state

    problem_file.write("Initial state: ")

    for disk in range(n_):
        for pile in range(1, m_):
            problem_file.write(proposition(disk, pile))

  # Goal state

    problem_file.write("\nGoal state: ")


    for disk in range(n_):
        for pile in range(m_ - 1):
            problem_file.write(proposition(disk, pile))

    problem_file.write("\n")

    problem_file.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
