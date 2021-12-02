filename = "input/day02.txt"
forward = 0
depth = 0
aim = 0
with open(filename) as file:
    for line in file:
        command = line.split(" ")
        instruction = command[0]
        moveit = int(command[1])
        if instruction == "forward":
            forward += moveit
            depth += aim * moveit
        elif instruction == "down":
            aim += moveit
        elif instruction == "up":
            aim -= moveit
        else:
            raise ValueError("this instruction is not known ", instruction)
        if depth < 0:
            raise ValueError("this submarine is flying!!")
    print "I'm at distance:{} and depth:{}".format(forward, depth)
    print "Solution => {}".format(forward * depth)
