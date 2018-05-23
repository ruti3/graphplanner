import sys

# Ai top
# Ai bottom
# Tablei Clear
# AiOnBj

def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    # Propososition
    domain_file.write("Propositions:\n")
    for disk in disks:
        domain_file.write(Clear(disk))
    # write TableClear Option
    for pile in pegs:
        domain_file.write(Clear(pile))

    # writing ON options
    for i in range(n_):
        for j in range(i): # j<i
            domain_file.write(On(disks[j],disks[i]))
        for pile in pegs:
            domain_file.write(On(disks[i], pile))

    domain_file.write("\nActions:\n")

    #move to clear pile
    for i in range(n_):
        for pile in pegs:
            for j in range(i+1,n_): # j<i
                moveBToA(disks[i], pile, disks[j], domain_file)
            for pile2 in pegs:
                if not pile==pile2:
                    moveBToA(disks[i], pile, pile2, domain_file)


    #move disk to disk while on top of disk
    for i in range(n_):
        for j in range(i+1,n_):
            for k in range(i+1,n_):
                if j != k:
                    moveBToA(disks[i], disks[j], disks[k], domain_file)
            for pile in pegs:
                moveBToA(disks[i], disks[j], pile, domain_file)


    domain_file.close()
def Clear(disk):
    return str(disk) + "Top "
def On(A,B):
    return str(A)+"-On-"+str(B)+" "

def moveBToA(fromDisk,toDisk,fromDiskOnDisk,domain_file):
    # Name
    domain_file.write("Name: MoveFrom-" + str(fromDisk) + "-To-" + str(toDisk)
                      +"-While-"+On(fromDisk,fromDiskOnDisk) + '\n')
    # pre
    domain_file.write("pre: " + Clear(fromDisk) +Clear(toDisk)+ On(fromDisk,fromDiskOnDisk))
    # add
    domain_file.write("\nadd: " + Clear(fromDiskOnDisk) + On(fromDisk,toDisk)+'\n')
    # delete
    domain_file.write("delete: " + Clear(toDisk) +On(fromDisk,fromDiskOnDisk)+ '\n')


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))]  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file

    # Initial state
    problem_file.write("Initial state: ")
    for pile in pegs[1:]:
        problem_file.write(Clear(pile))
    problem_file.write(Clear(disks[0]))

    for i in range(n-1):
        problem_file.write(On(disks[i], disks[i+1]))
    problem_file.write(On(disks[n-1],pegs[0]))

    # Goal state
    problem_file.write("\nGoal state: ")
    for pile in range(m-1):
        problem_file.write(Clear(pegs[pile]))

    problem_file.write(Clear(disks[0]))
    for i in range(n - 1):
        problem_file.write(On(disks[i], disks[i + 1]))
    problem_file.write(On(disks[n - 1], pegs[m_-1]))

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
