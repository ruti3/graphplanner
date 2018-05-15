import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    # Propososition
    domain_file.write("Propositions:\n")
    for disk in range(n):
        for pile in range(m):
            domain_file.write(proposition(disk, pile))
    domain_file.write("\nActions:\n")

    for disk in range(n):
        for pile in range(m):
            for to_pile in range(m):
                if not pile == to_pile:
                    move(disk, pile, to_pile, domain_file)


    domain_file.close()

def proposition(disk, piles):
    return "n"+str(disk)+"m"+str(piles)+" "

def move(disk, from_pile, to_pile, domain_file):
    # Name
    domain_file.write("Name: Mn"+str(disk)+"m"+str(from_pile)+str(to_pile)+'\n')
    # pre
    domain_file.write("pre: "+proposition(disk, to_pile))
    for i in range(disk):
        domain_file.write(proposition(i,from_pile)+proposition(i, to_pile))
    # add
    domain_file.write("\nadd: " + proposition(disk, from_pile)+ '\n')
    # delete
    domain_file.write("delete: " + proposition(disk, to_pile)+ '\n')

def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file

    # Initial state
    problem_file.write("Initial state: ")
    for disk in range(n):
        for pile in range(1,m):
            problem_file.write(proposition(disk, pile))
    # Goal state
    problem_file.write("\nGoal state: ")
    for disk in range(n):
        for pile in range(m-1):
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
