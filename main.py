from singlePrize import single_bfs, single_dfs, single_gbfs, single_astar
from multiPrize import multi_astar

def main():

    print("\nChoose a maze file:")
    print("1. 1prize-open.txt")
    print("2. 1prize-medium.txt")
    print("3. 1prize-large.txt")
    print("4. multiprize-tiny.txt")
    print("5. multiprize-small.txt")
    print("6. multiprize-medium.txt\n")
    firstinput = input("Enter the number to select a file: ")

    if firstinput == "1":
        print("\nChoose a search algorithm:")
        print("1. Breadth-first search")
        print("2. Depth-first search")
        print("3. Greedy best-first search")
        print("4. A* search.\n")
        secondinput = input("Enter the number to select an algorithm: ")
        if secondinput == "1":
            single_bfs("1prize-open.txt")
        elif secondinput == "2":
            single_dfs("1prize-open.txt")
        elif secondinput == "3":
            single_gbfs("1prize-open.txt")
        elif secondinput == "4":
            single_astar("1prize-open.txt")
        else:
            print("Not applicable input")

    elif firstinput == "2":
        print("\nChoose a search algorithm:")
        print("1. Breadth-first search")
        print("2. Depth-first search")
        print("3. Greedy best-first search")
        print("4. A* search.\n")
        secondinput = input("Enter the number to select an algorithm: ")
        if secondinput == "1":
            single_bfs("1prize-medium.txt")
        elif secondinput == "2":
            single_dfs("1prize-medium.txt")
        elif secondinput == "3":
            single_gbfs("1prize-medium.txt")
        elif secondinput == "4":
            single_astar("1prize-medium.txt")
        else:
            print("Not applicable input")

    elif firstinput == "3":
        print("\nChoose a search algorithm:")
        print("1. Breadth-first search")
        print("2. Depth-first search")
        print("3. Greedy best-first search")
        print("4. A* search.\n")
        secondinput = input("Enter the number to select an algorithm: ")
        if secondinput == "1":
            single_bfs("1prize-large.txt")
        elif secondinput == "2":
            single_dfs("1prize-large.txt")
        elif secondinput == "3":
            single_gbfs("1prize-large.txt")
        elif secondinput == "4":
            single_astar("1prize-large.txt")
        else:
            print("Not applicable input")

    elif firstinput == "4":
        multi_astar("multiprize-tiny.txt")

    elif firstinput == "5":
        multi_astar("multiprize-small.txt")

    elif firstinput == "6":
        multi_astar("multiprize-medium.txt")

    else:
        print("Not applicable input")

if __name__ == "__main__":
    main()